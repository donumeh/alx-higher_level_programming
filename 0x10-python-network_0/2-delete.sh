#!/bin/bash
# Bash Script that sends a DELETE request to the URL
[[ $# -eq 1 ]] && curl -X DELETE "$1"
