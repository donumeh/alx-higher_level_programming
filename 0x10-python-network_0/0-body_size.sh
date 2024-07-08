#!/bin/bash
# Request a url and gets size
[ $# -eq 1 ] && curl -sI "$1" | grep -i Content-Length | awk '{print $2}' || echo "Usage: $0 <URL>"
