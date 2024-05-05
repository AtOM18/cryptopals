ascii_range = list(range(97, 123)) + [32]

def score_gen(byte_string, key):
    out_byte = b""
    for x in byte_string:
        out_byte += bytes([x ^ key[0]])
    p = 0
    for y in out_byte:
        if y in ascii_range:
            p += 1
    return (p, out_byte)

result_bytes = ""
max_score = 0
with open("4.txt", "r") as file:
    for line in file:
        input_bytes = bytes.fromhex(line.strip())
        scores = []
        for i in range(256):
            key = i.to_bytes(1, byteorder='big')
            score, decrypted = score_gen(input_bytes, key)
            scores.append((score, decrypted, key))
        top_score, top_decrypted, top_key = max(scores, key=lambda x: x[0])
        if top_score > max_score:
            max_score = top_score
            result_bytes = top_decrypted
            best_key = top_key

print("Decrypted string:", result_bytes.decode('utf-8'))
print("Key:", best_key)
