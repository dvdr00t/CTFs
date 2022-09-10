def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

def decryption(ciphertext):
    plaintext = b''
    
    for c in ciphertext:
        for guess in range(256):
            if ((123 * guess + 18) % 256) == c:
                plaintext += int.to_bytes(guess, 1, 'big')
                break
    
    return plaintext
    
if __name__ == '__main__':
    
    # Reading encrypted message
    with open('msg.enc', 'r') as f_in:
        ciphertext = bytes.fromhex(f_in.readline())
    f_in.close()
    
    # Decrypt the message
    plaintext = decryption(ciphertext)
    print(plaintext.decode().split('\n')[1])
    