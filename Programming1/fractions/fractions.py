# In this exercise, you will first write a Python class Fraction for representing rational numbers, i.e. fractions.
#
# You will then use your class to evaluate simple arithmetic expressions involving fractions.
#
# An instance of your class should represent a single rational number. Your class should include the following operations:
#
# An initializer that constructs a Fraction from a numerator and denominator, which will both be integers.
#
# The denominator will never be zero.
#
# Methods add, sub, mul and div that can add, subtract, multiply or divide two Fraction objects, returning a new Fraction.
#
# Division by zero should return None.
#
# A magic method __repr__ that converts a Fraction to a string.
#
# If the Fraction represents an integer, the string should be a simple decimal number.
#
# Otherwise the string should have the form "8/3" or "-5/2", for example.
#
# A minus sign, if present, should always be at the beginning of the string.
#
# The output fraction must be in simplified form, e.g. "1/2" rather than "3/6".
import math, sys

class Fraction:
    def __init__(self, numerator, denominator):
        if math.gcd(numerator, denominator) != 1:
            self.numerator = numerator // math.gcd(numerator, denominator)
            self.denominator = denominator // math.gcd(numerator, denominator)
        else:
            self.numerator = numerator
            self.denominator = denominator

    def __repr__(self):
        if self.numerator == 0 or None:
            return "0"
        if self.numerator % self.denominator == 0:
            return str(self.numerator)
        elif self.denominator == 0:
            return "invalid"
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def add(self, new_fraction):
        if self.denominator == new_fraction.denominator:
            return Fraction(self.numerator + new_fraction.numerator, self.denominator)
        # if not same, find the lcm of the denominators and multiply the corresponding multipliers for each side
        else:
            multiple = math.lcm(self.denominator, new_fraction.denominator)
            left_m = multiple // self.denominator
            right_m = multiple // new_fraction.denominator
            return Fraction((self.numerator * left_m) + (new_fraction.numerator * right_m), multiple)

    def subtract(self, new_fraction):
        if self.denominator == new_fraction.denominator:
            return Fraction(self.numerator - new_fraction.numerator, self.denominator)
        else:
            multiple = math.lcm(self.denominator, new_fraction.denominator)
            left_m = multiple // self.denominator
            right_m = multiple // new_fraction.denominator
            return Fraction((self.numerator * left_m) - (new_fraction.numerator * right_m), multiple)

    def multiply(self, new_fraction):
        if new_fraction.denominator == 0:
            return "invalid"
        else:
            return Fraction((self.numerator * new_fraction.numerator), (self.denominator * new_fraction.denominator))

    def divide(self, new_fraction):
        if new_fraction.numerator == 0:
            return "invalid"
        else:
            return Fraction((self.numerator * new_fraction.denominator), (self.denominator * new_fraction.numerator))

def identify(x):
    if x == '\ ':
        return 'divide'
    elif x == '*':
        return 'multiply'
    elif x == '+':
        return 'add'
    elif x == '-':
        return 'sub'


def parse(expression, operators=["*", r"\ ".strip(), "+", "-"]):
    stack = ['']  # start with empty string on stack
    for exp in expression:
        if exp in operators:
            stack.append(exp) 
            stack.append(" ")# place operator as new element on stack
        elif exp != " ":  # not a space
            stack[-1] += exp  # append to last element on stack

    return stack

num = ''

for x in sys.stdin.readlines():
    if x == '':
        pass
    else:
        num += x


for line in num.replace(" ", "").split("\n"):

    if line == "":
        break

    expression = parse(line)
    if len(expression) == 0:
        pass
    elif len(expression) == 1:
        print(expression)
    else:
        left_exp = expression[0].strip()
        operator = expression[1]
        right_exp = expression[2].strip()

        if len(left_exp) > 2 and not left_exp.isnumeric():
            left_num = expression[0].split("/")[0]
            left_den = expression[0].split("/")[1]
            fraction1 = Fraction(int(left_num), int(left_den))
        else:
            left = expression[0]
            fraction1 = Fraction(int(left), 1)

        if len(right_exp) > 2 and not right_exp.isnumeric():
            right_num = expression[2].split("/")[0]
            right_den = expression[2].split("/")[1]
            fraction2 = Fraction(int(right_num), int(right_den))
        else:
            right = expression[2]
            fraction2 = Fraction(int(right), 1)

        if operator == r"\ ".strip():
            print(fraction1.divide(fraction2))
        elif operator == '*':
            print(fraction1.multiply(fraction2))
        elif operator == '+':
            print(fraction1.add(fraction2))
        elif operator == '-':
            print(fraction1.subtract(fraction2))




    # first = Fraction(curr_line[0])

# print(num)
# operator = getattr(Fraction, x)



