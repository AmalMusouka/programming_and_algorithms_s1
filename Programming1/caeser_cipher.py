shift = int(input())
word = input()

new = []

for letter in word:
    letter = letter.upper()
    if "A" <= letter <= "Z":
        new.append(chr((ord(letter) - ord("A") + shift) % 26 + ord("A")))
    else:
        new.append(letter)

print("".join(new))
