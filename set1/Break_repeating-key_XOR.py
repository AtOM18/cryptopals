import base64
from itertools import combinations

def hamming_code(i, j):
    dif = 0
    #first we take the byte xor of individual character
    byte_result= i^j
    while(byte_result>0):
        #count the no of 1s in the xor bit
        #until it is zero
        dif+=byte_result&1
        byte_result>>=1
    return dif

def find_key_size(ciphertext):
    Maxkeysize = 40
    chunk_size = 4 #we will take 4 chunks of key size, and take combinations of two at once and average the normalized sum
    key_results = []
    for key_size in range(2, Maxkeysize):
        distances=[]
        chunks=[]
        for j in range(0, chunk_size*key_size ,key_size):
            chunks+= [ciphertext[j:j+key_size]]
        for a, b in combinations(chunks, 2):   
            distance = sum(hamming_code(ai, bi) for ai, bi in zip(a,b))
            ndistance = distance/key_size
            distances.append(ndistance)
        key_results.append((key_size, sum(distances)/len(distances)))
    return min(key_results, key=lambda x: x[1]) #returning the key size and the normalized value


def single_byte_xor(ciphertext):
    ascii_range=list(range(65,122))+[32] #all the letters in the ascii table
    sum = 0
    key = b""
    for i in range(2**8): #for every possible key byte
        key_byte = i.to_bytes(1, byteorder='big')
        out_text = b""
        for x in ciphertext:
            out_text += bytes([x^key_byte[0]])
        p = 0
        for y in out_text: #checking which output text contains the most about of ascii characters
            if y in ascii_range:
                p+=1
        if p>sum:
            sum = p
            key = key_byte[0]
    return key


def finding_key(ciphertext, key_size):
    blocks = [ciphertext[i::key_size] for i in range(key_size)] #containing the bytes of the first character of the key
    key = [single_byte_xor(block) for block in blocks] #finding key value of each byte one by one
    return key


def decipher(ciphertext):
    output=b""
    key_size = find_key_size(ciphertext) #finding the key length
    key = finding_key(ciphertext, key_size[0]) #finding the key
    j = 0
    for i in ciphertext: #xoring each byte with each key byte
        output += bytes([i^key[j]])
        j = (j+1)%len(key)
    print(output.decode('utf-8'))

with open("6.txt", "r") as file:
    b64 = file.read()

ciphertext = base64.b64decode(b64) #bytes
decipher(ciphertext)



