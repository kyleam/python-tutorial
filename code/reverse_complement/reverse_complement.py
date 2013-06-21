#!/usr/bin/env python3


def reverse_complement(sequence):
    """Return the reverse complement of `sequence`

    Parameters
    ----------
    sequence : iterable  ## REV: why not just call this a `str`?
        can consist of G, C, A, or T
    """
    basemap = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([basemap[base] for base in reversed(sequence)])

if __name__ == '__main__':
    assert reverse_complement('ATGC') == 'GCAT'

    ## a list works, too
    assert  reverse_complement(['A', 'T', 'G', 'C']) == 'GCAT'
