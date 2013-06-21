#!/usr/bin/env python3
"""Functions for working with nucleotide sequences
"""
from codon_mapping import codon_to_aminoacid


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


def calculate_gc_ratio(sequence, precision=2):
    """Calculate the ratio of `sequence` that consits of a G or C nucleotide

    Parameters
    ----------
    sequence : iterable  ## REV: why not just call this a `str`?
        G/C elements must be represented as uppercase "G" or "C"
    precision : int
        number of digits to preserve after decimal point
    """
    gc_bases = [base for base in sequence if base in ['G', 'C']]

    # The content between [] above is called a "list comprehension". It
    # achieves the same result as
    #
    #   gc_bases = []
    #   for base in sequence:
    #       if base in ['G', 'C']:
    #           gc_bases.append(base)

    return round((len(gc_bases)) / len(sequence), precision)

    # Python 3 versus Python 2 difference in division
    # -----------------------------------------------
    # In python 2, dividing an int by an int does not include the
    # remainder, so 3/2 results is 1, not 1.5. In order to get a float
    # as the result, at least on of the numbers in the calculation needs
    # to be a float. The return statement could be rewritten like this
    # to be compatible with python 2:
    #
    #   return round(float(len(gc_bases)) / len(sequence), precision)


def translate(sequence, codon_table=None):
    """Translate DNA sequence into amino acid sequence

    Parameters
    ----------
    sequence : iterable
        elements must be either A, T, C, or G. Gapped sequence is not
        permitted. Should be a multiple of 3.
    codon_table : dict or None
        mappings of codon strings to amino acids. If None, standard
        mappings are used.

    Returns
    -------
    amino acid sequence (str)
    """
    if len(sequence) % 3 != 0:
        raise ValueError('Sequence is not multiple of 3')
    if codon_table is None:
        codon_table = codon_to_aminoacid

    aaseq = []
    for codon in _by_codon(sequence):
        aaseq.append(codon_table[codon])
    return ''.join(aaseq)


def _by_codon(sequence):
    """Return sequence elements by codon (i.e., by 3)

    If sequence is not a multiple of 3, elements extra tail elements are
    discarded.
    """
    codon = []
    for base in sequence:
        codon.append(base)
        if len(codon) == 3:
            yield ''.join(codon)
            codon = []

if __name__ == '__main__':
    ## tests (only executed if you run this script, not if you import it)

    ## reverse complement tests ##

    assert reverse_complement('ATGC') == 'GCAT'
    ## a list works, too
    assert  reverse_complement(['A', 'T', 'G', 'C']) == 'GCAT'

    ## gc ratio tests ##

    assert calculate_gc_ratio('GGCC') == 1
    assert calculate_gc_ratio('GGAA') == 0.5
    assert calculate_gc_ratio('AAAA') == 0

    ## test precision argument
    assert calculate_gc_ratio('GTATAT') == 0.17
    assert calculate_gc_ratio('GTATAT', 3) == 0.167

    ## what if a list is given instead of a string?
    assert calculate_gc_ratio(['G', 'A']) == 0.5

    ## lowercase given instead of capital letters
    assert calculate_gc_ratio('gggg') != 1

    print('All tests passed')
