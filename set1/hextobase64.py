import base64
data_in_hex = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw = base64.b16decode(data_in_hex, casefold=True)
result= base64.b64encode(raw)
print(result)

