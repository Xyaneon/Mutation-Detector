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
# Last modified: 10/15/2014

class ResultsOutput:
    def __init__(self, output_file=""):
        """Constructor for ResultsOutput object.
        If output_file is supplied, direct all output to that file."""
        self.output_file = output_file

    def write_output(self, string):
        """Sends the given string to the appropriate output."""
        if self.output_file:
            try:
                with open(self.output_file, 'a') as f:
                    f.write(string + "\n")
            except IOError:
                print "Error: could not open the file:", self.output_file
                exit(1)
        else:
            print string
