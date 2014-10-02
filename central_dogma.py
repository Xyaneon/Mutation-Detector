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
# Last modified: 10/2/2014

import re
from string import find, maketrans

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

start_codon = 'AUG'
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

def _find_start_codon(rna):
    """Finds the first start codon in the provided RNA sequence.
    It's assumed that the 5' end comes first in the given sequence.
    The start codon position is returned (0-based).
    If no start codon is found, -1 is returned."""
    return find(rna.upper(), start_codon)

def _find_first_stop_codon(rna):
    """Looks for the first stop codon in the given RNA sequence.
    The stop codon position is returned (0-based).
    This function assumes that position 0 holds the start codon.
    If no stop codon is found, return -1."""
    position = 3
    while position < rna.length:
        try:
            if rna[position:position + 3] in stop_codons:
                return position
            position += 3
        except IndexError:
            return -1
    return -1

def trim_to_coding_rna(rna):
    """Trims the given RNA sequence, 5' first, to the part which actually codes
    for the protein."""
    if rna.length < 3:
        # Too short to code for anything
        return ""
    start_position = _find_start_codon(rna)
    if start_position == -1:
        # No start codon found, so no resulting protein sequence
        return ""
    rel_rna = rna[start_position:]
    stop_position = _find_first_stop_codon(rel_rna)
    if stop_position != -1:
        rel_rna = rel_rna[:stop_position]
    return rel_rna

def translate_sequence(rna, single_letter_mode=True):
    """Translates the given RNA sequence into a amino acid sequence (protein).
    This assumes that the 5' end comes first.
    The amino acid sequence is returned, N end first."""
    rel_rna = trim_to_coding_rna(rna)
    if rel_rna == "":
        return ""
    protein = ""
    mode_selector = 1 if single_letter_mode else 0
    amino_acids = dict((re.escape(codon), amino_acid[mode_selector])
                        for codon, amino_acid in codon_table.iteritems())
    pattern = re.compile("|".join(amino_acids.keys()))
    protein = pattern.sub(lambda m: amino_acids[re.escape(m.group(0))], rel_rna)
    return protein

def transcribe_coding_sequence(dna):
    """Transcribes the given DNA coding sequence."""
    base_in = "AT"
    base_out = "UA"
    transcription_table = maketrans(base_in, base_out)
    return original.translate(transcription_table)

def reverse_sequence(strand):
    """Reverses the given strand comprised of single letters.
    This basically switches whether the 5'/N or 3'/C end comes first."""
    return strand[::-1]

if '__name__' == '__main__':
    # Unit testing.
    # From BioBackground section, p.37, of our class textbook.
    non_template_dna = "CGAAGGAATGCACGCCTATTAGGGACCC"
    template_dna     = "GCTTCCTTACGTGCGGATAATCCCTGGG"
    rna              = "CGAAGGAAUGCACGCCUAUUAGGGACCC"
    coding_sequence  = "AUGCACGCCUAUUAG"
    protein_3letter  = "MetHisAlaTyr"
    protein_1letter  = "MHAY"

    # Test above functions
    if non_template_dna != complement_DNA(template_dna):
        print "complement_dna function test failed"
        print "\ttemplate:", template_dna
        print "\tresult  :", complement_DNA(template_dna)
    elif transcribe_coding_sequence(non_template_dna) != rna:
        print "transcribe_coding_sequence function test failed"
        print "\trna     :", rna
        print "\tresult  :", transcribe_coding_sequence(non_template_dna)
    elif _find_start_codon(rna) != 7:
        print "_find_start_codon function test failed"
        print "\trna     :", rna
        print "\tresult  :", _find_start_codon(rna)
    else:
        print "Unit testing passed for central_dogma module."
