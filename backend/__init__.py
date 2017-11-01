
def encrypt(This_key_is_awesome, message):  #better way of doing it cause it doesn't repeat
    encrypted_message = []
    for i, c in enumarate(message): #assaning a number for every character
        key_c = ord(key[i % len(This_key_is_awesome)])   #ord() string representing one Unicode character
        message_c = ord (c)
        encrypted_message.append(chr((message_c + key_c) %127))
         #we are adding the message and the encryption key converted in Unicode character. The % is used to keep the resulting chr in the 7-bit ascii range
         #Think about % here like the clock: when it's x hours later than y 'o clock, it's (x+y) % 12 'o clock.) for afte ->
         #chr() a character (a string) whose Unicode code point is the integer i and after adding all of this to the list
    return ''.join(encrypted_message)


def decrypt(This_key_is_awesome,encrypted_message):
    message = []
     for i, c in enumerated(encrypted_message):
         key_c = ord(key[i % len(This_key_is_awesome)])
         encoded_c = ord(c)
         message.append(chr((message_c - key_c) %127)) #we are reverse engeneering the encrypted message
    return''.join(message)


def process_user_query(query_string):
    if __name__ == '__main__':  #so we can run it as a module the hole thing
        This_key_is_awesome = 'This_is_my_awsome_secret_key'
        message = query_string
        encrypted = encrypt(This_key_is_awesome, message)
        decrypted = decrypt(This_key_is_awesome, encrypted_message)
        return {'Message:': repr(message), 'Key:': repr(This_key_is_awesome),'Encrypted:': repr(encrypted_message),'Decrypted:': repr(encrypted_message)}
