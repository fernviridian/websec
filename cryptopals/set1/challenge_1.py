#! /usr/bin/env python2.7
import base64

# Convert hex to base64
s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

end_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hex_data = s.decode("hex")

import base64

encoded = base64.b64encode(hex_data)
assert(end_result == encoded)
print encoded
