#!/bin/bash
# This Script sends a POST request to the URL with some variables.
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" $1
