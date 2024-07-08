#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a GET request to the URL and get the size of the body in bytes
SIZE=$(curl -sI "$URL" | grep -i content-length | awk '{print $2}' | tr -d '\r')

echo "$SIZE"

