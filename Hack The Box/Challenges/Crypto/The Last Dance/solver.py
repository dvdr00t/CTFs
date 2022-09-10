'''
ChaCha20 encryption with same IV
'''

def xor(b1, b2):
	return bytes([b1[i] ^ b2[i % len(b2)] for i in range(len(b1))])


def exploit():

	message = b"Our counter agencies have intercepted your messages and a lot "
	message += b"of your agent's identities have been exposed. In a matter of "
	message += b"days all of them will be captured"

	file = open('crypto_the_last_dance/out.txt', 'r')
	iv = bytes.fromhex(file.readline()[:-1])
	message_enc = file.readline()[:-1]
	flag_enc = file.readline()

	print(f'[+] message is: {message.decode()}')
	print(f'[+] IV is: {iv}')
	print(f'[+] message encrypted is: {message_enc.encode()} with length of {len(message_enc) / 2}')
	print(f'[+] flag encrypted is: {flag_enc.encode()} with length of {len(flag_enc) / 2}')

	print()
	print('[.] reused-nonce attack: C1 xor C2 = P1 xor P2')
	xored_plaintext = xor(bytes.fromhex(message_enc), bytes.fromhex(flag_enc))
	flag = xor(message, xored_plaintext)
	print()
	print(f'[!] flag is: {flag[:len(flag_enc)//2].decode()}')

if __name__ == '__main__':
	exploit()