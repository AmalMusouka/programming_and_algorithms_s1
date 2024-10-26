import sys

for line in sys.stdin:
    if ">" in line:
        base1, base2 = line.split(">")
    else:
        num = line.strip()

        result = 0
        if num == "0":
            print("0")
        else:
            for digit in num:
                if digit.isdigit():
                    d = int(digit)
                    result = result * int(base1)
                    result = result + d
                else:
                    d = ord(digit) - 87
                    result = result * int(base1)
                    result = result + d
            s = ""
            while result != 0:
                rem = result % int(base2)
                if rem >= 10:
                    s = chr(rem + 87) + s
                else:
                    s = str(rem) + s
                result = result // int(base2)

            print(s)
