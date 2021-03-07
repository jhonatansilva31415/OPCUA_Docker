#!/bin/sh

echo "Waiting for server..."

while ! nc -z server 4840; do
  sleep 0.1
done

echo "Server started"

ls 

python client.py