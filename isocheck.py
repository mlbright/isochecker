#!/usr/bin/env python

import sys
import os
import os.path
import hashlib
from subprocess import Popen, PIPE

def process(cmd, block_size=1024*1024):
    checksum = hashlib.md5()
    fd = Popen(cmd,shell=True,stdout=PIPE).stdout
    try:
        while True:
            chunk = fd.read(block_size)
            if not chunk:
                break
            checksum.update(chunk)
    finally:
        fd.close()    
    return checksum.hexdigest()

if __name__ == "__main__":
    process(cmd="dd if=/dev/cdrom")
