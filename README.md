# Stackdriver Logging as a microservice using Mazzy
![Mazzh](https://img.shields.io/badge/mazzy-compiled-orange.svg)
![Docker Build Status](https://img.shields.io/badge/Dockerfile-automated-blue.svg)

Access the Stackdriver Logging API (Google Cloud Logging APIs) via the Mazzy service developed by Prowl.

## Usage
```coffee
logs = stackdriver entries_list projects: ['foo'] 
                                filter: 'advanced filters'
                                order_by: 'timestamp desc'
                                page_size: 100
                                page_token: 'xxxx'
                                json_return: 'json output'
log info msg: logs
```

Any questions or any information on Mazzy please email Montana at the following email address: inqueries@getprowl.com.
