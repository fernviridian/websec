#! /usr/bin/env python2.7

# challenge 2

from binascii import unhexlify

#Write a function that takes two equal-length buffers and produces their XOR combination.
#If your function works properly, then when you feed it the string:
input_string = '1c0111001f010100061a024b53535009181c'
#... after hex decoding, and when XOR'd against:

def xor(a, b):
  result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
  return '{:x}'.format(result)     # convert back to hexadecimal

xor_string = '686974207468652062756c6c277320657965'

output = xor(input_string, xor_string)

#... should produce:
expected = '746865206b696420646f6e277420706c6179'
assert(output == expected)
