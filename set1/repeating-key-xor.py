# Given string
string = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

# Key
key = "ICE"

# Convert string and key to bytes
string_bytes = string.encode()
key_bytes = key.encode()

# XOR each byte of the string with corresponding byte of the key
output = b""
j = 0
for i in string_bytes:
    output += bytes([i ^ key_bytes[j]])
    j = (j + 1) % len(key_bytes)

# Print the hexadecimal representation of the encrypted string
print(output.hex())

