#!/usr/bin/env python3
"""Merge two files by a common key column

usage: merge_on_key.py KEY FILE FILE [FILE ...]

arguments:
  KEY                header name to use as key
  FILE               file to merge
                     FILE should have KEY as a header name
                     and must be comma-delited.

Key must be present in all files listed

example
-------

file1.csv:
  person,age
  Mary,23
  John,19
file2.csv:
  person,job
  Mary,lawyer
  John,DJ

$ python merge_on_key.py person file1.csv file2.csv
person,age,job
John,19,DJ
Mary,23,lawyer
-------

TODO: What are some ways this could be improved?
"""
import sys
from collections import defaultdict


def process_file(fname, key, keyfields, nonkey_headers):
    """Process file for storing key values

    Parameters
    ----------
    fname : str
        filename
    key : str
        column name to use as key
    keyfields : dict
        dictionary to store field information
    nonkey_headers : list
        list to store non-key header information
    """
    with open(fname) as fh:
        headers = fh.readline().strip().split(',')
        keycol = headers.index(key)

        headers.pop(keycol)
        nonkey_headers.extend(headers)

        store_key_values(fh, keycol, keyfields)


def store_key_values(fh, keycol, keyfields):
    for line in fh:
        fields = line.strip().split(',')
        key = fields.pop(keycol)
        keyfields[key] += fields


def output_merged(keyname, keyfields, nonkey_headers):
    print(','.join([keyname] + nonkey_headers))
    for key, fields in keyfields.items():
        print(','.join([key] + fields))

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(__doc__)

    key, *files = sys.argv[1:]  # python3-specific

    keyfields = defaultdict(list)
    nonkey_headers = []
    for fname in files:
        process_file(fname, key, keyfields, nonkey_headers)

    output_merged(key, keyfields, nonkey_headers)
