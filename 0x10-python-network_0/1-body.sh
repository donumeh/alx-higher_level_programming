#!/bin/bash
# Sends a GET request to the URL and displays the body of the response
if [[ $# -eq 1 ]]
then
	status_code=$(curl -sI "$1" | head -n 1 | tr ' ' '\n' | tail -n 2 | head -n 1)
	
	if [[ $status_code -eq "200" ]]
	then
		curl -sg "$1"
		exit
	else
		exit 1
	fi
fi
