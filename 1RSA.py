#!/bin/python

from pwn import *

p = process("/challenge/run")

p.recvuntil(b"(public) n = 0x")
n = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"(public) e = 0x")
e = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"(private) d = 0x")
d = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"Flag Ciphertext (hex): ")
flag = int(p.recvline().strip().decode(), 16)

pt = pow(flag, d, n)

print(pt)