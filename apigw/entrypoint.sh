#!/bin/bash -l

export PORT=${PORT:-8080}
export THREAD_COUNT=${THREAD_COUNT:-2}


echo ".................   FLASKAPP-PROM   ......................"
echo ""
echo " Starting application via waitress-server"
echo ""
echo "            PORT: ${PORT}"
echo "         THREADS: ${THREAD_COUNT}"
echo "         VERSION: $(cat VERSION)"
echo ""
echo "..........................................................."

waitress-serve --port ${PORT} --threads ${THREAD_COUNT} main:app

echo "Exit code is: $?"
echo ""
echo "Cleaning variables"
unset PORT
echo "-"
unset THREAD_COUNT
echo "-"
echo "Finished, thanks for using"