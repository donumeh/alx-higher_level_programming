#!/bin/bash
# this script sends an OPTIONS req to a URL
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
