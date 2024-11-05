import sys

final = ""

for line in sys.stdin.readlines():  # reading input
    newline = "".join(line.replace("\n", " "))  # join the input strings into one line
    final += newline  # We add the line to a new string

newline = final.replace(". ", ".\n")
# replacing the spaces after a "." with newline
print(newline.strip())  # to remove leading whitespaces and extra newlines
