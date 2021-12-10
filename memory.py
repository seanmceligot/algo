import time
import os
import sys
import mmap
d = 1000

print(f"variable address {id(d):x}")
print(f"sys.stdout address {id(sys.stdout):x}")
print(f"static {id('hello world'):x}")
print(f"0 {id(0):x}")
with open("Makefile", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    time.sleep(1)
    with open(f"/proc/{os.getpid()}/maps", "r") as f:
        print(f.read())



