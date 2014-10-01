# This file is part of Mutation-Detector.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# Mutation-Detector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Mutation-Detector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Mutation-Detector. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 9/25/2014

codon_table = {
    'GCA': ('Ala', 'A'), 'GCC': ('Ala', 'A'), 'GCG': ('Ala', 'A'),
    'GCU': ('Ala', 'A'),
    'GGA': ('Gly', 'G'), 'GGC': ('Gly', 'G'), 'GGG': ('Gly', 'G'),
    'GGU': ('Gly', 'G'),
    'CCA': ('Pro', 'P'), 'CCC': ('Pro', 'P'), 'CCG': ('Pro', 'P'),
    'CCU': ('Pro', 'P'),
    'CGA': ('Arg', 'R'), 'CGC': ('Arg', 'R'), 'CGG': ('Arg', 'R'),
    'CGU': ('Arg', 'R'),
    'AGA': ('Arg', 'R'), 'AGG': ('Arg', 'R'),
    'CAC': ('His', 'H'), 'CAU': ('His', 'H'),
    'AGC': ('Ser', 'S'), 'AGU': ('Ser', 'S'), 'UCA': ('Ser', 'S'),
    'UCC': ('Ser', 'S'),
    'UCG': ('Ser', 'S'), 'UCU': ('Ser', 'S'),
    'AAU': ('Asn', 'N'), 'AAC': ('Asn', 'N'),
    'AUA': ('Ile', 'I'), 'AUC': ('Ile', 'I'), 'AUU': ('Ile', 'I'),
    'ACA': ('Thr', 'T'), 'ACC': ('Thr', 'T'), 'ACG': ('Thr', 'T'),
    'ACU': ('Thr', 'T'),
    'GAC': ('Asp', 'D'), 'GAU': ('Asp', 'D'),
    'CUA': ('Leu', 'L'), 'CUC': ('Leu', 'L'), 'CUG': ('Leu', 'L'),
    'CUU': ('Leu', 'L'),
    'UUA': ('Leu', 'L'), 'UUG': ('Leu', 'L'),
    'UGG': ('Trp', 'W'),
    'UGC': ('Cys', 'C'), 'UGU': ('Cys', 'C'),
    'GAA': ('Glu', 'E'), 'GAG': ('Glu', 'E'),
    'AAA': ('Lys', 'K'), 'AAG': ('Lys', 'K'),
    'AUG': ('Met', 'M'),
    'UAC': ('Tyr', 'Y'), 'UAU': ('Tyr', 'Y'),
    'GUA': ('Val', 'V'), 'GUC': ('Val', 'V'), 'GUG': ('Val', 'V'),
    'GUU': ('Val', 'V'),
    'CAA': ('Gln', 'Q'), 'CAG': ('Gln', 'Q'),
    'UUC': ('Phe', 'F'), 'UUU': ('Phe', 'F'),
    'UAA': ('Stop', '_'), 'UAG': ('Stop', '_'), 'UGA': ('Stop', '_')
}

def complementDNA(original):
    """Creates the complement of the given DNA strand."""
    result = ""
    for base in original:
        if base == 'A':
            result += 'T'
        elif base == 'T':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
    return result

def complementRNA(original):
    """Creates the complement of the given RNA strand."""
    result = ""
    for base in original:
        if base == 'A':
            result += 'U'
        elif base == 'U':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
    return result

def translate(rna):
    """Translates the given RNA sequence."""
    # TODO

def transcribe(dna):
    """Transcribes the given DNA sequence."""
    result = ""
    for base in original:
        if base == 'A':
            result += 'U'
        elif base == 'T':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
    return result

def reverse(strand):
    """Reverses the given strand."""
    return strand[::-1]

if '__name__' == '__main__':
    # TODO: Unit testing.
