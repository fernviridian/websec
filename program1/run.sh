#! /bin/sh

docker run --rm -v "${PWD}:/app" websec-mongo python /app/program1.py
