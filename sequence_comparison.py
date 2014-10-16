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

from results_output import ResultsOutput

def produce_shorthand(c1, index, c2):
    '''Formats the given characters and position into a shorthand mutation.'''
    return c1 + str(index + 1) + c2 + '\n'

def compare_sequences(seq1, seq2, output):
    '''Compares two single-character sequences for substitution mutations.
    Returns the number of mutations found.
    Expects both sequences to be of the same length.'''
    if len(seq1) != len(seq2):
        difference = abs(len(seq1) - len(seq2))
        differ_len = "Sequences are not the same length; "
        differ_len += "they differ by " + str(difference) + " character"
        if difference == 1:
            differ_len += "."
        else:
            differ_len += "s."
        output.write_output(differ_len)
    mctr = 0
    shorthands = ""
    for i in range(0, min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            # Output mutation shorthand, e.g., K136R
            shorthands += produce_shorthand(seq1[i], i, seq2[i])
            mctr += 1
    if len(seq1) > len(seq2):
        for i in range(len(seq2), len(seq1)):
            shorthands += produce_shorthand(seq1[i], i, '-')
            mctr += 1
    elif len(seq1) < len(seq2):
        for i in range(len(seq1), len(seq2)):
            shorthands += produce_shorthand('-', i, seq2[i])
            mctr += 1
    output.write_output(shorthands)
    if mctr == 0:
        identical = "No mismatches found - strings are identical"
        output.write_output(identical)
    elif mctr == 1:
        output.write_output(str(mctr) + " mutation found.")
    else:
        output.write_output(str(mctr) + " mutations found.")
    return mctr
