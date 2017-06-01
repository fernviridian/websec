#! /usr/bin/env python2.7

#Single-byte XOR cipher
#The hex encoded string:

from challenge_3 import *

# get all strings from the file

encrypted_strings = []

with open("4.txt") as f:
    encrypted_strings = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    encrypted_strings = [x.strip() for x in encrypted_strings] 

top_scores = {}

for string in encrypted_strings:
  scores = {}
  unhex = binascii.unhexlify(string)
  for char in range(0, 256):
    result = try_char(unhex, char)
    scores[char] = score(result)
  max_score = max(scores.values())
  top_scores[string] = max_score

# now we need to compare all teh top scores to get the hex-encoded string that best matched
best_score_string = max(top_scores, key=top_scores.get)
unhex = binascii.unhexlify(best_score_string)

# confirm and decrypt

if __name__ == '__main__':
  # build small structure to hold scores
  scores = {}
  for char in range(0, 256):
    # try all the chars in ascii
    result = try_char(unhex, char)
    scores[char] = score(result)

  # get the top score
  the_key = max(scores, key=scores.get)

  # get the decrypted data
  print "Data: {}".format(try_char(unhex, the_key))
