Mutation-Detector
=================

Homework 2 for MCS 5603 Intro to Bioinformatics. Written in Python 2.7 and hosted on GitHub with Dr. Miller's permission.

This program compares two sequences in FASTA format for mutations. It can perform transcription and/or translation of input DNA and mRNA sequences and do comparisons to count mutations, provided that the sequences are the same length (there is no insertion/deletion mutation support).

## Usage ##

In a terminal, type

    python Mutation_Detector.py -h

for a full list of usage options.

Generally, you will enter the program name followed by two input files, each preceded by two arguments indicating whether the file contains a coding/template DNA strand and whether it is 3' or 5'. For example:

    python Mutation_Detector.py coding 5 sequence1.fasta template 3 sequence2.fasta

You can indicate whether you want comparisons done on the DNA, mRNA or amino acid sequences, or all three. For example, to compare only mutations in the DNA:

    python Mutation_Detector.py coding 3 sequence1.fasta coding 3 sequence2.fasta -d

To compare mutations only in amino acid sequences (default if no comparison options are specified):

    python Mutation_Detector.py coding 3 sequence1.fasta coding 3 sequence2.fasta --protein

To compare mutations in all sequence types:

    python Mutation_Detector.py coding 3 sequence1.fasta coding 3 sequence2.fasta --compare-as all

(As you might have guessed, there are three ways to enter each option, and they cannot be mixed. The program also cannot go backwards on the [central dogma of molecular biology](http://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology); for instance, if supplied only with mRNA sequences, it cannot compare the DNA mutations and will produce an error if you try.)

An output file may be optionally specified using `-o` or `--output`:

    python Mutation_Detector.py coding 5 sequence1.fasta template 3 sequence2.fasta -o results.txt

When directing output to an output file, nothing will be printed to the terminal unless an error occurs.

If any mutations are found, they will be output in a shorthand format, consisting of the original character, the index, and the new character.

## License ##

[GNU GPLv3](http://www.gnu.org/copyleft/gpl.html)
