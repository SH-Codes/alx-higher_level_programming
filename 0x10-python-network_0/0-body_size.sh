#!/bin/bash
#The following Bash script takes in a URL

curl -s "$1" | wc -c
