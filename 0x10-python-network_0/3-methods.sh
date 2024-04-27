#!/bin/bash
# This Script displays all the HTTP methods the server will accept
curl -sX OPTIONS $1
