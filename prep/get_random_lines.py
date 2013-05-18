#!/usr/bin/env python
"""get random lines

usage: get_random_lines.py NUMBER FILE OUTFILE
"""
import sys
import random

if len(sys.argv) != 4:
    print(__doc__)
    sys.exit()

numrandom = int(sys.argv[1])
infile = sys.argv[2]
outfile = sys.argv[3]

lines = open(infile).readlines()
random.shuffle(lines)

with open(outfile, 'w') as outfh:
    for idx, line in enumerate(lines):
        if idx >= numrandom:
            break
        outfh.write(line)
