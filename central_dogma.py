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
# Last modified: 10/1/2014

import re
from string import maketrans

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

stop_codons = ['UAA', 'UAG', 'UGA']

def complementDNA(original):
    """Creates the complement of the given DNA strand."""
    base_in = "ATGC"
    base_out = "TACG"
    complementation_table = maketrans(base_in, base_out)
    return original.translate(complementation_table)

def complementRNA(original):
    """Creates the complement of the given RNA strand."""
    base_in = "AUGC"
    base_out = "UACG"
    complementation_table = maketrans(base_in, base_out)
    return original.translate(complementation_table)

def translate_sequence(rna, single_letter_mode=True):
    """Translates the given RNA sequence."""
    start = rna.upper().find('AUG')
    position = start
    protein = ""
    current_codon = 'AUG'
    mode_selector = 1 if single_letter_mode else 0
    output_codons = dict((re.escape(codon), amino_acid[mode_selector]) \
                          for codon, amino_acid in codon_table.iteritems())
    pattern = re.compile("|".join(output_codons.keys()))
    # TODO: trim RNA sequence to first start codon and first following stop
    protein = pattern.sub(lambda m: output_codons[re.escape(m.group(0))], text)
    return protein

def transcribe_sequence(dna):
    """Transcribes the given DNA sequence."""
    base_in = "ATGC"
    base_out = "UACG"
    transcription_table = maketrans(base_in, base_out)
    return original.translate(transcription_table)

def reverse_sequence(strand):
    """Reverses the given strand comprised of single letters."""
    return strand[::-1]

if '__name__' == '__main__':
    # TODO: Unit testing.
