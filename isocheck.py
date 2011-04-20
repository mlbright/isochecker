#!/usr/bin/env python

import sys
import os
import os.path
import hashlib
from subprocess import Popen, PIPE

def checksum(cmd="dd if=/dev/cdrom", block_size=2**20):
    cs = hashlib.md5()
    fd = Popen(cmd,shell=True,stdout=PIPE).stdout
    try:
        while True:
            chunk = fd.read(block_size)
            if not chunk:
                break
            cs.update(chunk)
    finally:
        fd.close()    
    return cs.hexdigest()

if __name__ == "__main__":
    print checksum()
