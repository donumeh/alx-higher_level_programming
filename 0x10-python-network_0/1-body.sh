#!/bin/bash
# Bash script that takes in usr and uses get to request to the URL
[[ -eq 1 ]] && curl -L -X GET "$1"
