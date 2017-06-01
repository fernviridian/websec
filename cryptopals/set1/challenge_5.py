#! /usr/bin/env python2.7
import binascii

s1 = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = "ICE"
#Encrypt it, under the key "ICE", using repeating-key XOR.

def repeat_key_xor(string, key):
  string = string.strip()
  # make the key the right length for repeating
  key_string = (len(string) / len(key) + 1) * key
  # trim key to length if needed
  key_string = key_string[:len(string)]
  encrypted = ""
  for i, char in enumerate(string):
    encrypted += chr(ord(char) ^ ord(key_string[i]))

  # hex encode it
  return binascii.hexlify(encrypted)
    
  #chr(ord("1") ^ ord("a"))
  
#In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

s1_enc = repeat_key_xor(s1, key)
assert("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f" == s1_enc)

print "Tests passed!"
