#!/bin/python

from pwn import *


o = process("/challenge/run")

o.recvuntil(b"e = 0x")
e = int(o.recvline().strip().decode(), 16)

o.recvuntil(b"p = 0x")
p = int(o.recvline().strip().decode(), 16)

o.recvuntil(b"q = 0x")
q = int(o.recvline().strip().decode(), 16)

 
o.recvuntil(b'Flag Ciphertext (hex): ')
flag=int(o.recvline().strip().decode(), 16)
 
n = p * q
phi = (p - 1)*(q - 1)

d = pow(e, -1, phi)

pt = pow(flag, d, n)
print(pt)