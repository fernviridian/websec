#! /bin/sh

docker run -it --rm -v "${PWD}:/app" websec-mongo python /app/program1.py $1
