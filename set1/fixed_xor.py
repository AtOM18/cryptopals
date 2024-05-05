str1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
str2 = bytes.fromhex("686974207468652062756c6c277320657965")

result = b""
for a,b in zip(str1, str2):
    result+=bytes([a^b])
print(result)
if(result == bytes.fromhex("746865206b696420646f6e277420706c6179")):
    print("valid")
else:
    print("invalid")
