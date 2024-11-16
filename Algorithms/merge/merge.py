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


file_path_1 = extract_arguments()[0]
file_path_2 = extract_arguments()[1]
file_path_3 = extract_arguments()[2]

with open(file_path_1, 'r') as file_1, open(file_path_2, 'r') as file_2, open(file_path_3, 'w') as file_3:
    line_1 = file_1.readline()
    line_2 = file_2.readline()
    line_list = []


    while line_1 != "" or line_2 != "":
        if line_1 == "" or (line_2 != "" and line_2 < line_1):
            file_3.write(line_2)
            line_2 = file_2.readline()

        elif line_2 == "" or  (line_1 != "" and line_1 < line_2):
            file_3.write(line_1)
            line_1 = file_1.readline()
