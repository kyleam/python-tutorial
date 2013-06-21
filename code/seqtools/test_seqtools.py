"""Tests for seqtools.py

Install
-------

Use pip to install py.test.

  pip install pytest

Depending on your setup, `pip` above may be `pip3`.

Running
-------

With terminal or command prompt in the seqtools directory, run

  py.test

For more output, run

  py.test --verbose
"""
import pytest
import seqtools as st


## reverse complement tests


def test_reverse_complement_with_str():
    assert st.reverse_complement('ATGC') == 'GCAT'


def test_reverse_complement_with_list():
    assert st.reverse_complement(['A', 'T', 'G', 'C']) == 'GCAT'


## gc ratio tests


def test_calculate_gc_ratio_all_gcs():
    assert st.calculate_gc_ratio('GGCC') == 1


def test_calculate_gc_ratio_half_gcs():
    assert st.calculate_gc_ratio('GGAA') == 0.5


def test_calculate_gc_ratio_no_gc():
    assert st.calculate_gc_ratio('AAAA') == 0


def test_calculate_gc_ratio_default_precision():
    assert st.calculate_gc_ratio('GTATAT') == 0.17


def test_calculate_gc_ratio_nondefault_precision():
    assert st.calculate_gc_ratio('GTATAT', 3) == 0.167


def test_calculate_gc_ratio_with_list():
    assert st.calculate_gc_ratio(['G', 'A']) == 0.5


def test_calculate_gc_ratio_lowercase_fail():
    assert st.calculate_gc_ratio('gggg') != 1


## translate


def test_by_codon():
    result = list(st._by_codon('AAATTT'))
    assert result == ['AAA', 'TTT']


def test_by_codon_with_list():
    result = list(st._by_codon(['A', 'A', 'A', 'T', 'T', 'T']))
    assert result == ['AAA', 'TTT']


def test_by_codon_not_multiple_of_three():
    ## elements that are not part of a triplet should be truncated
    result = list(st._by_codon('AAAT'))
    assert result == ['AAA', ]


def test_seqtools_not_multiple_of_three():
    with pytest.raises(ValueError):
        st.translate('A')


def test_seqtools_with_default_codon_table():
    result = st.translate('GTACCC')
    expected = 'VP'
    assert result == expected


def test_seqtools_with_default_codon_table_with_list():
    result = st.translate(['G', 'T', 'A', 'C', 'C', 'C'])
    expected = 'VP'
    assert result == expected


def test_seqtools_with_supplied_codon_table():
    codon_table = {'AAA': '!', 'TTT': '$'}
    result = st.translate('AAATTT', codon_table=codon_table)
    expected = '!$'
    assert result == expected
