#!/bin/bash
# This Script takes in a URL as argument and sends a request to the URL
curl -s $1 | wc -c
