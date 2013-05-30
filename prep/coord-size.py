#!/usr/bin/env python
import fileinput

for line in fileinput.input():
    start, stop = [int(i) for i in line.split('\t')[3:5]]
    size = stop - start
    if size > 100000:
        print(line.strip())
