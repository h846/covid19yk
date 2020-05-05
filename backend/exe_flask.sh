#!/bin/bash

# gunicorn (AP server) run shell script for python flask programs
exec /home/yassi/.pyenv/shims/gunicorn --chdir /usr/share/nginx/covid19yk/backend/ api:api