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
from seqtools import reverse_complement, calculate_gc_ratio

## reverse complement tests


def test_reverse_complement_with_str():
    assert reverse_complement('ATGC') == 'GCAT'


def test_reverse_complement_with_list():
    assert  reverse_complement(['A', 'T', 'G', 'C']) == 'GCAT'


## gc ratio tests


def test_calculate_gc_ratio_all_gcs():
    assert calculate_gc_ratio('GGCC') == 1


def test_calculate_gc_ratio_half_gcs():
    assert calculate_gc_ratio('GGAA') == 0.5


def test_calculate_gc_ratio_no_gc():
    assert calculate_gc_ratio('AAAA') == 0


def test_calculate_gc_ratio_default_precision():
    assert calculate_gc_ratio('GTATAT') == 0.17


def test_calculate_gc_ratio_nondefault_precision():
    assert calculate_gc_ratio('GTATAT', 3) == 0.167


def test_calculate_gc_ratio_with_list():
    assert calculate_gc_ratio(['G', 'A']) == 0.5


def test_calculate_gc_ratio_lowercase_fail():
    assert calculate_gc_ratio('gggg') != 1
