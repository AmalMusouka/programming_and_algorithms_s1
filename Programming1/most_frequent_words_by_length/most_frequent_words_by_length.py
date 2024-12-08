import sys


# In this exercise, a word is any sequence of consecutive letters that is not preceded or followed by a letter.
#
# Letters are any characters in the set {'A' .. 'Z', 'a' .. 'z'}. Case is insignificant: "AARDVARK" and "aardvark" are the same word.
#
# Read text from standard input until it ends, and determine the most frequent word for every word length encountered in the input.
#
# Write these to the output, in increasing order of word length, along with the number of occurrences of each word.
#
# Follow the output format illustrated in the sample output below. Write all output words in lowercase, regardless of the case in which they were seen in the input.
#
# If for any word length there are multiple words that tie for being most frequent, write all of them on the same line in alphabetical order.
#
# Notice that if a word occurs only once, you must write "1 occurrence" (not "1 occurrences").

def words_from_string(string):
    words = []

    word = ''
    for letter in string:

        if ord(letter) > ord("z") or ord(letter) < ord("A"):
            if word != '':
                words.append(word)
                word = ''
                continue
        else:
            word += letter


    return words


def solve(input):
    words = words_from_string(input)
    tally = {}
    for word in words:
        key = len(word)

        if key not in tally:
            tally[key] = []

        tally[key].append(word)

    return tally


def most_frequent_words(arr, n):

    freq = 0
    res = ""

    for i in range(0, n):
        count = 1
        for j in range(i + 1, n):
            if arr[j] == arr[i]:
                count += 1

        if count > freq:
            res = (arr[i]) + " "
            freq = count
        elif count == freq:
            res += (arr[i]) + " "
            freq = count

    return str(res), freq


# input_string = """Some glory in their birth, some in their skill,
# Some in their wealth, some in their bodies' force,
# Some in their garments, though new-fangled ill,
# Some in their hawks and hounds, some in their horse;
# And every humour hath his adjunct pleasure,
# Wherein it finds a joy above the rest:
# But these particulars are not my measure;
# All these I better in one general best.
# Thy love is better than high birth to me,
# Richer than wealth, prouder than garments' cost,
# Of more delight than hawks or horses be;
# And having thee, of all men's pride I boast:
# Wretched in this alone, that thou mayst take
# All this away and me most wretched make."""

input_string = ""
for line in sys.stdin.readlines():
    input_string += line




number_of_words = (solve(input_string.lower()))
sorted_words = sorted(number_of_words.items())


# print(sorted_words)

for key, value in sorted_words:
    new = most_frequent_words(sorted(value),len(value))
    if new[1] == 1:
        print(f"length {key}: {new[0]}({new[1]} occurrence)")
    else:
        print(f"length {key}: {new[0]}({new[1]} occurrences)")















