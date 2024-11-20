import sys

# #Read text from standard input until it ends, and determine the 20 words that appear most frequently in it.
#
# Write each of these words along with its number of occurrences to standard output, in descending order of frequency.
#
# If two different words have the same number of occurrences, you may choose either of them for the top 20 words as necessary, and you may write them in either order if they are both in the top 20.
#
# In this exercise, we consider a word to be any sequence of consecutive letters that is not preceded or followed by a letter.
#
# Letters are only from the Latin alphabet, i.e. A through Z without any accent marks. When comparing two words, the difference between lowercase and uppercase letters is considered to be significant.
#
# Note: You won't be able to use Python's split() method to split each input line into words, since it considers words to be separated by whitespace, which is different from the definition above.
#
# You will need to iterate over the input lines and find the words yourself.
#
# Each output line should contain a word and its number of occurrences, separated by a single space.
#
# If the input contains fewer than 20 different words, the output should contain only as many words as occur in the input.




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

input_string = " "
for line in sys.stdin.readlines():
    input_string += line



number_of_words = (words_from_string(input_string))
i = 0
for key, value in number_of_words:
    if i == 20:
        break
    else:
        print(value, key)
        i += 1