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



def merge(a, b, c):
    i = j = 0

    for k in range(len(c)):
        if j == len(b):
            c[k] = a[i]
            i += 1
        elif i == len(a):
            c[k] = b[j]
            j += 1
        elif a[i] > b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1

def merge_sort(list):
    if len(list) < 2 :
        return

    mid = len(list) // 2

    a = list[:mid]
    b = list[mid:]

    merge_sort(a)
    merge_sort(b)

    merge(a, b, list)

# def sort_by_length(list):




def words_from_string(string):
    word = ''
    word_count = dict()
    for letter in string:

        if ord(letter) > ord("z") or ord(letter) < ord("A") :
            if word != '':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                word = ''
                continue
        else:
            word += letter
    output = [(v, k) for k, v in word_count.items()]
    merge_sort(output)
    return output

# input_string = " "
# for line in sys.stdin.readlines():
#     input_string += line

input_string = """Some glory in their birth, some in their skill,
Some in their wealth, some in their bodies' force,
Some in their garments, though new-fangled ill,
Some in their hawks and hounds, some in their horse;
And every humour hath his adjunct pleasure,
Wherein it finds a joy above the rest:
But these particulars are not my measure;
All these I better in one general best.
Thy love is better than high birth to me,
Richer than wealth, prouder than garments' cost,
Of more delight than hawks or horses be;
And having thee, of all men's pride I boast:
Wretched in this alone, that thou mayst take
All this away and me most wretched make."""


test_dict = {'is': [1, 2], 'gfg': [3], 'best': [1, 3, 4]}

number_of_words = (words_from_string(input_string))
# print(sorted(number_of_words, reverse=True, key=lambda x: len(x) > 3))
# for key, value in number_of_words:
#     print(value, key)