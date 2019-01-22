# Stackdriver Logging as a microservice using Mazzy

![Mazzh](https://img.shields.io/badge/mazzy-compiled-orange.svg)
[![Docker Build Status](https://img.shields.io/badge/Dockerfile-automated-blue.svg)

Access the Stackdriver Logging API (Google Cloud Logging APIs) via a Mazzy service.

## Usage
```coffee
# Storyscript
logs = stackdriver entries_list projects: ['foo'] 
                                filter: 'advanced filters'
                                order_by: 'timestamp desc'
                                page_size: 100
                                page_token: 'xxxx'
log info msg: logs
```
