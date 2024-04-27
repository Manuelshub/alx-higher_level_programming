#!/bin/bash
# This Script sends a GET request to a URL, and the a header variable must be sent with a value of 98.
curl -sH "X-School-User-Id: 98" $1
