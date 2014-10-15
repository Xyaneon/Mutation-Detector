Mutation-Detector
=================

Homework 2 for MCS 5603 Intro to Bioinformatics. Written in Python 2.7 and hosted on GitHub with Dr. Miller's permission.

This program compares two sequences in FASTA format for mutations. It can perform transcription and translation of input DNA sequences and do comparisons to count mutations, provided that the sequences are the same length (there is no insertion/deletion mutation support).

## Usage ##

In a terminal, type

    python Mutation_Detector.py -h

for a full list of usage options.

Generally, you will enter the program name followed by two input files, each preceded by two arguments indicating whether the file contains a coding/template DNA strand and whether it is 3' or 5'. For example:

    python Mutation_Detector.py coding 5 sequence1.fasta template 3 sequence2.fasta

An output file may be optionally specified:

    python Mutation_Detector.py coding 5 sequence1.fasta template 3 sequence2.fasta -o results.txt

## License ##

[GNU GPLv3](http://www.gnu.org/copyleft/gpl.html)
