from json import loads, dumps
def encrypt(This_key_is_awesome, message):  #better way of doing it cause it doesn't repeat
    encrypted_message = []
    for i, c in enumerate(message): #assaning a number for every character
        key_c = ord(This_key_is_awesome[i % len(This_key_is_awesome)])   #ord() string representing one Unicode character
        message_c = ord (c)
        encrypted_message.append(chr((message_c + key_c) %127))
         #we are adding the message and the encryption key converted in Unicode character. The % is used to keep the resulting chr in the 7-bit ascii range
         #Think about % here like the clock: when it's x hours later than y 'o clock, it's (x+y) % 12 'o clock.) for afte ->
         #chr() a character (a string) whose Unicode code point is the integer i and after adding all of this to the list
    return dumps(''.join(encrypted_message))


def decrypt(This_key_is_awesome,encrypted_message):
    encrypted_message = loads(encrypted_message)
    message = []
    for i, c in enumerate(encrypted_message):
         key_c = ord(This_key_is_awesome[i % len(This_key_is_awesome)])
         encoded_c = ord(c)
         message.append(chr((encoded_c - key_c) %127)) #we are reverse engeneering the encrypted message
    return''.join(message)


def process_user_query(query_string):
    q = query_string.splitlines()
    if q[0] == 'encrypt':
        return encrypt(q[1],q[2])
    else:
        return decrypt(q[1],q[2])



#comand encrypt or  decrypt
#key
#message
