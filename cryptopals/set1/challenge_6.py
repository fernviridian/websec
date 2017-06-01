#! /usr/bin/env python2.7
import binascii
import base64

#https://stackoverflow.com/questions/12226846/count-letter-differences-of-two-strings
def diff_letters(a,b):
#  import pdb; pdb.set_trace()
  return sum ( a[i] != b[i] for i in range(len(a)) )

def hamming_distance(st1,st2):
    assert len(st2) == len(st2)
    #bin_x = ' '.join(format(ord(x), 'b') for x in st1).replace(" ", "")
    bin_x = ' '.join('{0:08b}'.format(ord(x), 'b') for x in st1).replace(" ", "")
    bin_y = ' '.join('{0:08b}'.format(ord(x), 'b') for x in st2).replace(" ", "")
    assert len(bin_x) == len(bin_y)
    #bin_x = bin(int(binascii.hexlify(x), 16))
    #bin_y = bin(int(binascii.hexlify(y), 16))
    return diff_letters(bin_x, bin_y)

def read_file():
  with open('6.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
  return data

def main():
  assert(hamming_distance("this is a test", "wokka wokka!!!") == 37)
  bindata = base64.b64decode(read_file())
  # is a str
  keysize_dict = {}

  for keysize in range(2, 40):
    first_chunk = bindata[:keysize]
    second_chunk = bindata[keysize:keysize*2]
    keysize_dict[keysize] = hamming_distance(first_chunk, second_chunk)/keysize

  # get the minimum key
  lowest = 999
  keysize = 0
  for key,value in keysize_dict.iteritems():
    if value <= lowest:
      lowest = value
      keysize = key
  print lowest, keysize

  # The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

  # Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
  x = "qwertyui"
  blocks, block_size = len(bindata), len(bindata)/keysize
  blocklist = [ bindata[i:i+block_size] for i in range(0, blocks, block_size) ]
  print blocklist
  print len(blocklist)

  #top_scores[string] = max_score
  #for key in keysize_dict:
  #   print key, keysize_dict[key]

  # Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

  #For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.


  #The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

if __name__ == "__main__":
  main()
