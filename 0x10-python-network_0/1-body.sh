#!/bin/bash
# Sends a GET request to the URL and displays the body of the response
[[ $# -eq 1 ]] && [[ $(curl -sI "$1" | head -n 1 | tr ' ' '\n' | tail -n 2 | head -n 1) -eq "200" ]] && curl -sg "$1"
