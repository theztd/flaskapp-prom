#!/bin/bash -l

waitress-serve --port ${PORT} --threads ${THREAD_COUNT} main:app
