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
# Last modified: 10/8/2014

import argparse

import central_dogma as cd
import sequence_comparison

parser = argparse.ArgumentParser()
parser.add_argument("infile1", help="file containing the first sequence " +
                    "in FASTA format", type=str)
parser.add_argument("infile2", help="file containing the second sequence " +
                    "in FASTA format", type=str)
parser.add_argument("--outfile", help="Filename for the output file", type=str)
args = parser.parse_args()

infile1, infile2 = args.infile1, args.infile2
outfile = ""
if args.outfile:
    outfile = args.outfile

# Read in sequences from FASTA files
# Ignore first line since that's just header info, not part of the sequence
lines1 = lines2 = []
sequence1 = sequence2 = ""
with open(infile1, 'r') as infile1_reading:
    lines1 = infile1_reading.readlines()[1:]
with open(infile2, 'r') as infile2_reading:
    lines2 = infile2_reading.readlines()[1:]
for line in lines1:
    sequence1 += line.upper().strip()
for line in lines2:
    sequence2 += line.upper().strip()

# Debug
print "Sequence 1:"
print sequence1
print "\nSequence 2:"
print sequence2

sequence1 = cd.reverse_sequence(sequence1)
sequence2 = cd.reverse_sequence(sequence2)

# Debug
print "Sequence 1:"
print sequence1
print "\nSequence 2:"
print sequence2

mRNA1 = cd.transcribe_coding_sequence(sequence1)
mRNA2 = cd.transcribe_coding_sequence(sequence2)

# Debug
print "mRNA 1:"
print mRNA1
print "\nmRNA 2:"
print mRNA2

aminoseq1 = cd.translate_sequence(mRNA1)
aminoseq2 = cd.translate_sequence(mRNA2)

# Debug
print "Amino Sequence 1:"
print aminoseq1
print "\nAmino Sequence 2:"
print aminoseq2

sequence_comparison.compare_amino_1letter(aminoseq1, aminoseq2, args.outfile)