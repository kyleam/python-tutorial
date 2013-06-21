""" import the program
>>> import bio_ys """

import sys

def reverse_complement(dna):
    """Return the reverse complementary sequence string

    Parameters
    dna : str
    """
    basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    # letters = list(dna)
    reverse_sequence = []
    # for base in reversed(letters)
    for base in dna[::-1]:
        reverse_sequence += basecomplement[base]
    return ''.join(reverse_sequence)

def calculate_gc_content(sequence):
    """Return gc content of the sequence

    Parameters
    sequence : str
    """
    n = 0
    # if 'C' in sequence or 'G' in sequence:
    for base in sequence:
        if base == 'C' or base == 'G':
            n += 1
    l = n/len(sequence)
    return '{:.2f}'.format(l)

###################################################
if __name__ == '__main__':
    print ('This has lots of functions. Use it.')

    print('Running tests...')

    assert reverse_complement("GGCA") == "TGCC"

    assert calculate_gc_content('AAAA') == '0.00'
    assert calculate_gc_content('AAAG') == '0.25'
    assert calculate_gc_content('AAGG') == '0.50'

    print('.... and it works!!!')
