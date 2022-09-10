import json
from pwn import *
from sympy.ntheory.modular import crt

# Data
HOST = '167.172.57.231'
PORT = 32452

def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

def egcd(a: int, b: int) -> tuple:
    '''
    Computes Bezout gcd()
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    

if __name__ == '__main__':
    
    # Connecting to receive the ciphertexts
    conn = remote(HOST, PORT)
    time_capsules = []
    for _ in range(5):
        question = conn.recvuntil(b') ')
        try:
            conn.sendline(b'Y')
        except:
            print('Ops...')

        response = conn.recv()
        time_capsules.append(json.loads(response[:-1].decode()))
    conn.close()
    

        
    
    # Hastad's Broadcast Attack
    n1 = int(time_capsules[0]['pubkey'][0], 16)
    n2 = int(time_capsules[1]['pubkey'][0], 16)
    n3 = int(time_capsules[2]['pubkey'][0], 16)
    n4 = int(time_capsules[3]['pubkey'][0], 16)
    n5 = int(time_capsules[4]['pubkey'][0], 16)
    
    C1 = int(time_capsules[0]['time_capsule'], 16)
    C2 = int(time_capsules[1]['time_capsule'], 16)
    C3 = int(time_capsules[2]['time_capsule'], 16)
    C4 = int(time_capsules[3]['time_capsule'], 16)
    C5 = int(time_capsules[4]['time_capsule'], 16)
    
    n = []
    n.append(n1)
    n.append(n2)
    n.append(n3)
    n.append(n4)
    n.append(n5)
    
    C = []
    C.append(C1)
    C.append(C2)
    C.append(C3)
    C.append(C4)
    C.append(C5)
    
    result = int(crt(n, C)[0])
    
    x = iroot(5, result)
    m = int.to_bytes(x, 1024, 'big')
    print('[!] Message recovered is: ', m.replace(b'\x00', b'').decode())