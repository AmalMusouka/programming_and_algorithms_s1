import sys

reminder = ""

for line in sys.stdin.readlines():  # reading input
    sentences = (reminder.replace("\n", " ") + line).split(".")
    reminder = sentences.pop()

    for sentence in sentences:
        print(sentence.strip() + ".")


# another solution

# sentence = ''
# for line in sys.stdin:
#     for c in line:
#         if sentence == '':
#             if not c.isspace():
#                 sentence += c
#             else:
#                 if c == '.':
#                     print(sentence + '.')
#                     sentence = ''
#                 elif c == '\n':
#                     sentence += ' '
#                 else:
#                     sentence += c
