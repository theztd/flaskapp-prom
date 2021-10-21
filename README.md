[![Deploy](https://github.com/theztd/flaskapp-prom/actions/workflows/deploy-nomad.yml/badge.svg)](https://github.com/theztd/flaskapp-prom/actions/workflows/deploy-nomad.yml)

# Microservidce nomad app (demo)

Simple demo application writen in [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Vue.js](https://vuejs.org) and [GOlang](https://golang.org) for playing with design concepts and technology. Application can reply via graphQL or REST api, uses websocket and is deployed via [nomadproject.io](https://nomadproject.io). 


```bash

                    +-----------+
                    |     FE    |
                    |  Vue app  |
                    +-----------+
                          | 
                          V
                    +-----------+
                    |   APIGW   |
                    |  GraphQL  |
                    |   Flask   |
                    +-----------+
                          |
                          V
      ------------------------------------------- Intranet
       |            |                  
       V            V
  +---------+  +---------+
  |   BE    |  |   AUTH  |
  |  Flask  |  |  Flask  |  
  +---------+  +---------+


```


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

