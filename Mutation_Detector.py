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
# Last modified: 10/16/2014

import argparse
import os.path

import central_dogma as cd
from results_output import ResultsOutput
import sequence_comparison

version = "v2.0.0"
desc = "Mutation Detector " + version
desc += "\nA utility for finding mutations between FASTA sequences."
infile_help="""
Takes three strings indicating 1) coding, template, or mRNA, 2) 3' or 5', and
3) filename.
"""

def is_coding_type(sequence_type):
    """Predicate returning True iff this is a coding DNA sequence type."""
    return sequence_type.lower() in ["c", "coding"]

def is_template_type(sequence_type):
    """Predicate returning True iff this is a template DNA sequence type."""
    return sequence_type.lower() in ["t", "template"]

def is_DNA_type(sequence_type):
    """Predicate returning True iff this is a DNA sequence type."""
    return is_coding_type(sequence_type) or is_template_type(sequence_type)

def is_mRNA_type(sequence_type):
    """Predicate returning True iff this is an mRNA sequence type."""
    return sequence_type.lower() in ["r", "mrna"]

def is_valid_type(sequence_type):
    """Predicate returning True iff this is a valid sequence type."""
    return is_DNA_type(sequence_type) or is_mRNA_type(sequence_type)

def is_valid_direction(sequence_direction):
    """Predicate returning True iff this is a valid sequence direction."""
    return sequence_direction in ["3", "3'", "5", "5'"]

def validate_sequence_options(seqopt1, seqopt2):
    """Checks the sequence options for validity."""
    sequence_type1 = seqopt1[0].lower()
    sequence_type2 = seqopt2[0].lower()
    if not is_valid_type(sequence_type1):
        print "Invalid type for first sequence:", sequence_type1
        exit(1)
    if not is_valid_type(sequence_type2):
        print "Invalid type for second sequence:", sequence_type2
        exit(1)
    sequence_direction1 = seqopt1[1].lower()
    sequence_direction2 = seqopt2[1].lower()
    if not is_valid_direction(sequence_direction1):
        print "Invalid direction for first sequence:", sequence_direction1
        exit(1)
    if not is_valid_direction(sequence_direction2):
        print "Invalid direction for second sequence:", sequence_direction2
        exit(1)
    path1 = seqopt1[2]
    path2 = seqopt2[2]
    if not os.path.exists(path1):
        print "First file does not exist:", path1
        exit(1)
    if not os.path.exists(path2):
        print "Second file does not exist:", path2
        exit(1)

#============================================================================
# Main program code
#============================================================================

# Set up commandline argument parser
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
                              help="Compare as proteins (default).",
                              action="store_true"
                             )
comparison_group.add_argument("-a", "--all",
                              help="Compare as DNA, mRNA, and protein.",
                              action="store_true"
                             )
comparison_group.add_argument("-c", "--compare-as",
                              help="Compare as DNA, mRNA, protein, or all.",
                              choices=["DNA", "mRNA", "protein", "all"],
                              type=str
                             )
args = parser.parse_args()

outfile = ""
if args.outfile:
    outfile = args.outfile
output = ResultsOutput(outfile)

# Verify commandline options
validate_sequence_options(args.infile1, args.infile2)
sequence_type1 = args.infile1[0].lower()
sequence_type2 = args.infile2[0].lower()
sequence_direction1 = args.infile1[1].lower()
sequence_direction2 = args.infile2[1].lower()
path1 = args.infile1[2]
path2 = args.infile2[2]
comparison_choice = "protein"
if args.compare_as:
    comparison_choice = args.compare_as
if args.DNA:
    comparison_choice = "DNA"
if args.mRNA:
    comparison_choice = "mRNA"
if args.protein:
    comparison_choice = "protein"
if args.all:
    comparison_choice = "all"

# Read in sequences from FASTA files
# Ignore first line since that's just header info, not part of the sequence
sequence1 = sequence2 = ""
try:
    with open(path1, 'r') as infile1_reading:
        lines1 = infile1_reading.readlines()[1:]
except IOError:
    print "Error: could not open first file:", path1
    exit(1)
try:
    with open(path2, 'r') as infile2_reading:
        lines2 = infile2_reading.readlines()[1:]
except IOError:
    print "Error: could not open second file:", path2
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
mRNA1 = mRNA2 = ""
protein1 = protein2 = ""
if is_DNA_type(sequence_type1):
    if is_template_type(sequence_type1):
        DNA1 = cd.complement_DNA(sequence1)
    elif is_coding_type(sequence_type1):
        DNA1 = sequence1
elif is_mRNA_type(sequence_type1):
    mRNA1 = sequence1
else:
    print "Unrecognized sequence type."
    exit(1)
if is_DNA_type(sequence_type2):
    if is_template_type(sequence_type2):
        DNA2 = cd.complement_DNA(sequence2)
    elif is_coding_type(sequence_type2):
        DNA2 = sequence2
elif is_mRNA_type(sequence_type2):
    mRNA2 = sequence2
else:
    print "Unrecognized sequence type."
    exit(1)

if comparison_choice in ["DNA", "all"]:
    if is_DNA_type(sequence_type1) and is_DNA_type(sequence_type2):
        if comparison_choice == "all":
            output.write_output("DNA sequence mutations:")
        sequence_comparison.compare_sequences(DNA1, DNA2, output)
        if comparison_choice == "DNA":
            exit(0)
    else:
        print "Cannot compare non-DNA input sequence(s) as DNA."
        exit(1)

if is_DNA_type(sequence_type1):
    mRNA1 = cd.transcribe_coding_sequence(DNA1)
if is_DNA_type(sequence_type2):
    mRNA2 = cd.transcribe_coding_sequence(DNA2)

if comparison_choice in ["mRNA", "all"]:
    if mRNA1 and mRNA2:
        if comparison_choice == "all":
            output.write_output("mRNA sequence mutations:")
        sequence_comparison.compare_sequences(mRNA1, mRNA2, output)
        if comparison_choice == "mRNA":
            exit(0)
    else:
        print "Cannot compare as mRNA sequences."
        exit(1)

if comparison_choice in ["protein", "all"]:
    protein1 = cd.translate_sequence(mRNA1)
    protein2 = cd.translate_sequence(mRNA2)
    if comparison_choice == "all":
        output.write_output("Amino acid sequence mutations:")
    sequence_comparison.compare_sequences(protein1, protein2, output)

exit(0)
