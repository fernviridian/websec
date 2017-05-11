#! /bin/sh

docker run -it --rm -v "${PWD}:/app" websec-brute python /app/program2.py $1
