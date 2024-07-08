#!/bin/bash
# takes a url and get request
curl -sL -w "%{http_code}" "$1" -o /tmp/body_file ; [[ $(tail -n1 /tmp/body_file) == "200" ]] && cat /tmp/body_file || true
