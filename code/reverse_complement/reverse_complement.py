#!/usr/bin/env python3


def reverse_complement(sequence):
    basemap = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([basemap[base] for base in reversed(sequence)])

if __name__ == '__main__':
    result =  reverse_complement('ATGC')
    assert result == 'GCAT'
