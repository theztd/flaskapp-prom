#!/bin/bash
# Generate randomly requests to random url (Graph data generator :-D)

for a in `seq 999999`; do for i in `seq $((RANDOM%20))`; do curl -kL "localhost:8080/url$((RANDOM%10)).json"; done; sleep $((RANDOM%5)); done
