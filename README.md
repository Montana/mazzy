# Using Mazzy as a Stackdriver micrologging service for Prowl

![Mazzy](https://img.shields.io/badge/mazzy-compiled-orange.svg)
![Mazzy Build Status](https://img.shields.io/badge/dockerbuild-automated-blue.svg)

Access the Stackdriver Logging API (Google Cloud Logging APIs) via the Mazzy service.

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
