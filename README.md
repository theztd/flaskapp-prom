[![Deploy](https://github.com/theztd/flaskapp-prom/actions/workflows/deploy-nomad.yml/badge.svg)](https://github.com/theztd/flaskapp-prom/actions/workflows/deploy-nomad.yml)

# flaskapp-prom

Simple demo application able to reply you via graphQL or REST api.


Available ENV parameters
------------------------
 * **PORT** - port where application should listen
 * **THREAD_COUNT** - count of thread pool
 * **UP** - set false when you want start maintanance mode
 * **DB_URI** - when db is present (sqlite example: sqlite:///develop.sqlite3)


Available endpoints
------------------- 
* /metrics - _url with prometheus metrics_
* /graphql - _graphql endpoint_
* /status - _json status page_
* /up - _simple enpoint to detect if app is up or down_

