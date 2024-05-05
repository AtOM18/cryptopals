input_bytes=bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
ascii_range=list(range(97,122))+[32]
result_msg = ""

sum=0
for i in range(2**8):
    key_byte = i.to_bytes(1, byteorder='big')
    out_text = b""
    for x in input_bytes:
        out_text += bytes([x^key_byte[0]])
    p=0
    for y in out_text:
        if y in ascii_range:
            p+=1
    if p>sum:
        sum = p
        result_msg = out_text

print(result_msg.decode('utf-8'))
