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
# Last modified: 10/14/2014

import argparse

import central_dogma as cd
import sequence_comparison

version = "v0.0.0"
desc = "Mutation Detector " + version
desc += "\nA utility for finding mutations between FASTA sequences."
infile_help="""
Takes three strings indicating coding or template, 3' or 5', and filename.
"""

def sequence_type_valid(sequence_type):
    """Predicate returning True iff this is a valid sequence type."""
    return sequence_type in ["t", "template",
                             "c", "coding",
                             "r", "mRNA"
                            ]

def sequence_type_is_DNA(sequence_type):
    """Predicate returning True iff this is a DNA sequence type."""
    return sequence_type in ["t", "template",
                             "c", "coding"
                            ]

def sequence_direction_valid(sequence_direction):
    """Predicate returning True iff this is a valid sequence direction."""
    return sequence_type in ["3", "3'",
                             "5", "5'"
                            ]

#============================================================================
# Main program code
#============================================================================

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("infile1", help=infile_help, nargs=3)
parser.add_argument("infile2", help=infile_help, nargs=3)
parser.add_argument("-o", "--outfile", help="Filename for the output file",
                    type=str)
comparison_group = parser.add_mutually_exclusive_group()
comparison_group.add_argument("-d", "--DNA",
                              help="Compare as 5' coding DNA.",
                              action="store_true"
                             )
comparison_group.add_argument("-r", "--mRNA",
                              help="Compare as mRNA.",
                              action="store_true"
                             )
comparison_group.add_argument("-p", "--protein",
                              help="Compare as proteins.",
                              action="store_true"
                             )
comparison_group.add_argument("-a", "--all",
                              help="Compare as DNA, mRNA, and proteins.",
                              action="store_true"
                             )
args = parser.parse_args()

outfile = ""
if args.outfile:
    outfile = args.outfile

# Verify commandline options
sequence_type1 = args.infile1[0].lower()
sequence_type2 = args.infile2[0].lower()
if not sequence_type_valid(sequence_type1):
    print "Invalid type for first sequence:", sequence_type1
    exit(1)
if not sequence_type_valid(sequence_type2):
    print "Invalid type for second sequence:", sequence_type2
    exit(1)
sequence_direction1 = args.infile1[1].lower()
sequence_direction2 = args.infile2[1].lower()
if not sequence_direction_valid(sequence_direction1):
    print "Invalid direction for first sequence:", sequence_direction1
    exit(1)
if not sequence_direction_valid(sequence_direction2):
    print "Invalid direction for second sequence:", sequence_direction2
    exit(1)

# Read in sequences from FASTA files
# Ignore first line since that's just header info, not part of the sequence
sequence1 = sequence2 = ""
try:
    with open(args.infile1[2], 'r') as infile1_reading:
        lines1 = infile1_reading.readlines()[1:]
except IOError:
    print "Error: could not open file:", args.infile1[2]
    exit(1)
try:
    with open(args.infile2[2], 'r') as infile2_reading:
        lines2 = infile2_reading.readlines()[1:]
except IOError:
    print "Error: could not open file:", args.infile2[2]
    exit(1)
for line in lines1:
    sequence1 += line.upper().strip()
for line in lines2:
    sequence2 += line.upper().strip()

# Process sequences after reading
if args.infile1[1] in ["3'", "3"]:
    sequence1 = cd.reverse_sequence(sequence1)
if args.infile2[1] in ["3'", "3"]:
    sequence2 = cd.reverse_sequence(sequence2)

DNA1 = DNA2 = ""
if sequence_type_is_DNA(sequence_type1):
    if sequence_type1 in ["t", "template"]:
        sequence1 = cd.complement_DNA(sequence1)
    DNA1 = sequence1
if sequence_type_is_DNA(sequence_type2):
    if sequence_type2 in ["t", "template"]:
        sequence2 = cd.complement_DNA(sequence2)
    DNA2 = sequence2

if args.DNA or args.all:
    sequence_comparison.compare_sequences(DNA1, DNA2, args.outfile)
    exit(0)

mRNA1 = cd.transcribe_coding_sequence(DNA1)
mRNA2 = cd.transcribe_coding_sequence(DNA2)

if args.mRNA or args.all:
    sequence_comparison.compare_sequences(mRNA1, mRNA2, args.outfile)
    exit(0)

aminoseq1 = cd.translate_sequence(mRNA1)
aminoseq2 = cd.translate_sequence(mRNA2)

if not (args.DNA or args.mRNA):
    sequence_comparison.compare_sequences(aminoseq1, aminoseq2, args.outfile)
