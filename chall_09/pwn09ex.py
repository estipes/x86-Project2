# coding: utf-8
from pwn import *
p=process("./chall_09")
payload = b"This isn't pwning this is reversing, life is a li"
p.sendline(payload)
p.interactive()
