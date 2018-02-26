#!/usr/bin/env python3
import binascii
key = "saiSsfzk"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    temp = bytes(r, "utf-8")
    return binascii.hexlify(temp)
    
