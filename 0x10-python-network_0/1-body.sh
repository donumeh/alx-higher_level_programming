#!/bin/bash
# Bash script that takes in usr and uses get to request to the URL
[[ $# -eq 1 ]] && url="$1" && while [[ $(curl -sI -o /dev/null -w "%{http_code}" "$url") =~ ^3 ]]; do url=$(curl -sI "$url" | grep -i "location:" | awk '{print $2}' | tr -d '\r'); done && [[ $(curl -sI -o /dev/null -w "%{http_code}" "$url") == "200" ]] && curl -sg "$url"
