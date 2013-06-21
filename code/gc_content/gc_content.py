#!/usr/bin/env python3


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

if __name__ == '__main__':
    ## tests (only executed if you run this script, not if you import it)
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
