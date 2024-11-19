import sys


# Write a program that reads one or more lines of text, and guesses whether the text is in English or Czech.
# In the input, Czech characters will be written without diacritical marks; for example, "pořád" will be written as "porad".
#
# To accomplish this task, compute the observed frequency of each letter in the input text,
# i.e. the number of occurrences of the letter divided by the total number of occurrences of all letters. Ignore case.
#
# The expected frequencies of letters in the English and Czech languages are as follows, as percentages.
# (You will need to divide the percentages by 100 to get frequencies in the range from 0 to 1.)

# Frequencies of letters A, B, ..., Z

en_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
           0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
           2.758, 0.978, 2.360, 0.150,  1.974, 0.074]

cz_freq = [8.421, 0.822, 0.740, 3.475, 7.562, 0.084, 0.092, 1.356, 6.073, 1.433,
           2.894, 3.802, 2.446, 6.468, 6.695, 1.906, 0.001, 4.799, 5.212, 5.727,
           2.160, 5.344, 0.016, 0.027, 1.043, 1.503]




def get_count(count_chars, freq):
    cz_sum = 0

    for i in range(len(freq)):
        cz_val = (freq[i]) / 100

        if i in count_chars.keys():
            for key, value in count_chars.items():
                if i == key:
                    cz_sum += ((value / number_of_char - cz_val) ** 2) / cz_val


        else:
            cz_sum += ((0 - cz_val) ** 2) / cz_val

    return cz_sum

input_string = ""

for line in sys.stdin:
    input_string += line

number_of_char = sum(i.isalpha() for i in input_string)
count_chars = dict()

for char in input_string:
    if char.isalpha():
        if ord(char.lower()) - 97 in count_chars:
            count_chars[ord(char.lower())-97] += 1
        else:
            count_chars[ord(char.lower())-97] = 1

eng = get_count(count_chars, en_freq)
cz = get_count(count_chars, cz_freq)

print(f"Match with English: {eng:.2f}")
print(f"Match with Czech: {cz:.2f}")

if eng > cz:
    print(f"Text is in Czech")
else:
    print(f"Text is in English")
