import sys

# Write a Python program that can merge two sorted files, writing the output to a third file.
#
# Your program will take three filenames as command-line arguments: the names of two input files, plus the name of an output file. The input files will already be sorted: the lines in each of these files will appear in alphabetical order.
#
# Read the input files and merge their contents, writing lines to the output file in sorted order.
#
# If the user specifies '-i' as the first command-line argument, the input files will be sorted case-insensitively, and you should also merge them in a case-insensitive way. (As a reminder, in a case-insensitive comparison uppercase and lowercase letters are considered to be identical.)
#
# Important: The input files may be larger than memory, so your solution may not read the entire contents of either file into memory all at once (e.g. in a list that holds all input lines). Instead, process the input incrementally.
#
# Assume that every line in the input files including the last line ends with a newline (i.e. '\n' or '\r\n'). Note that either input file might possibly be empty.


# TODO: process command line arguments






def extract_arguments():
    commands = sys.argv
    return commands[1], commands[2], commands[3]


print(extract_arguments())
