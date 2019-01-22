import json
import os
import sys
import tempfile
from datetime import datetime

from flask import Flask, make_response, request

from google.cloud import logging
from google.cloud.logging.entries import StructEntry, TextEntry

key_env_json_dict = 'GOOGLE_CREDENTIALS_JSON'


class EntryEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return str(o)

        return super(EntryEncoder, self).default(o)


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        creds_path = os.path.join(tempfile.mkdtemp(),
                                  'google-credentials.json')
        creds_file = open(creds_path, 'w+')
        creds_file.write(os.getenv(key_env_json_dict))
        creds_file.close()

        self.client = logging.Client.from_service_account_json(
            json_credentials_path=creds_path)

        os.remove(creds_path)

    def entries_list(self):
        req = request.get_json()
        # req can contain one of the following:
        # 1. projects - list
        # 2. filter - str
        # 3. order_by - either "timestamp asc" or "timestamp desc"
        # 4. page_size - int
        # 5. page_token - str

        req['filter_'] = req.pop('filter')
        all_entries = []
        entries = self.client.list_entries(**req)
        for entry in entries:
            if not (isinstance(entry, StructEntry) or
                    isinstance(entry, TextEntry)):
                print(f'Unsupported log entry class - {entry}')
                continue

            entry_ = {
                'insert_id': entry.insert_id,
                'severity': entry.severity,
                'timestamp': entry.timestamp,
                'payload': entry.payload
            }

            all_entries.append(entry_)

            if len(all_entries) >= req.get('page_size', sys.maxsize):
                break

        return self.end(all_entries)

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res, cls=EntryEncoder))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv(key_env_json_dict) is None:
        print(f'Environment variable {key_env_json_dict} not found.')
        sys.exit(1)

    handler = Handler()
    handler.app.add_url_rule('/entries/list', 'entries_list',
                             handler.entries_list,
                             methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
