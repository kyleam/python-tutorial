"""codon/amino acid mappings
from http://www.hgmd.cf.ac.uk/docs/cd_amino.html
"""

codon_to_aminoacid = {
    'TTT': 'F',
    'TTC': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'TCT': 'S',
    'TCC': 'S',
    'TCA': 'S',
    'TCG': 'S',
    'TAT': 'Y',
    'TAC': 'Y',
    'TAA': 'X',
    'TAG': 'X',
    'TGT': 'C',
    'TGC': 'C',
    'TGA': 'X',
    'TGG': 'W',
    'CTT': 'L',
    'CTC': 'L',
    'CTA': 'L',
    'CTG': 'L',
    'CCT': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAT': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGT': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'ATT': 'I',
    'ATC': 'I',
    'ATA': 'I',
    'ATG': 'M',
    'ACT': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAT': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGT': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GTT': 'V',
    'GTC': 'V',
    'GTA': 'V',
    'GTG': 'V',
    'GCT': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAT': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGT': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}

## from http://www.hgmd.cf.ac.uk/docs/cd_amino.html
#####################################################
# TTT     Phenylalanine   Phe     F                 #
# TTC     Phenylalanine   Phe     F                 #
# TTA     Leucine Leu     L                         #
# TTG     Leucine Leu     L                         #
# TCT     Serine  Ser     S                         #
# TCC     Serine  Ser     S                         #
# TCA     Serine  Ser     S                         #
# TCG     Serine  Ser     S                         #
# TAT     Tyrosine        Tyr     Y                 #
# TAC     Tyrosine        Tyr     Y                 #
# TAA     Termination (ochre)     Ter     X         #
# TAG     Termination (amber)     Ter     X         #
# TGT     Cysteine        Cys     C                 #
# TGC     Cysteine        Cys     C                 #
# TGA     Termination (opal or umber)     Ter     X #
# TGG     Tryptophan      Trp     W                 #
# CTT     Leucine Leu     L                         #
# CTC     Leucine Leu     L                         #
# CTA     Leucine Leu     L                         #
# CTG     Leucine Leu     L                         #
# CCT     Proline Pro     P                         #
# CCC     Proline Pro     P                         #
# CCA     Proline Pro     P                         #
# CCG     Proline Pro     P                         #
# CAT     Histidine       His     H                 #
# CAC     Histidine       His     H                 #
# CAA     Glutamine       Gln     Q                 #
# CAG     Glutamine       Gln     Q                 #
# CGT     Arginine        Arg     R                 #
# CGC     Arginine        Arg     R                 #
# CGA     Arginine        Arg     R                 #
# CGG     Arginine        Arg     R                 #
# ATT     Isoleucine      Ile     I                 #
# ATC     Isoleucine      Ile     I                 #
# ATA     Isoleucine      Ile     I                 #
# ATG     Methionine      Met     M                 #
# ACT     Threonine       Thr     T                 #
# ACC     Threonine       Thr     T                 #
# ACA     Threonine       Thr     T                 #
# ACG     Threonine       Thr     T                 #
# AAT     Asparagine      Asn     N                 #
# AAC     Asparagine      Asn     N                 #
# AAA     Lysine  Lys     K                         #
# AAG     Lysine  Lys     K                         #
# AGT     Serine  Ser     S                         #
# AGC     Serine  Ser     S                         #
# AGA     Arginine        Arg     R                 #
# AGG     Arginine        Arg     R                 #
# GTT     Valine  Val     V                         #
# GTC     Valine  Val     V                         #
# GTA     Valine  Val     V                         #
# GTG     Valine  Val     V                         #
# GCT     Alanine Ala     A                         #
# GCC     Alanine Ala     A                         #
# GCA     Alanine Ala     A                         #
# GCG     Alanine Ala     A                         #
# GAT     Aspartate       Asp     D                 #
# GAC     Aspartate       Asp     D                 #
# GAA     Glutamate       Glu     E                 #
# GAG     Glutamate       Glu     E                 #
# GGT     Glycine Gly     G                         #
# GGC     Glycine Gly     G                         #
# GGA     Glycine Gly     G                         #
# GGG     Glycine Gly     G                         #
# n/a     Aspartate or Asparagine n/a     B         #
# n/a     Glutamate or Glutamine  n/a     Z         #
#####################################################
