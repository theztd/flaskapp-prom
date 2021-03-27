#!/bin/bash -l

waitress --port ${PORT} --threads ${THREAD_COUNT} main:app
