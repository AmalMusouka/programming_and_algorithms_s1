import sys

reminder = ""

for line in sys.stdin.readlines():  # reading input
    sentences = (reminder.replace("\n", " ") + line).split(".")
    reminder = sentences.pop()

    for sentence in sentences:
        print(sentence.strip() + ".")
