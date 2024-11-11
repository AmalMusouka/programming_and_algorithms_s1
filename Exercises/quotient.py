x = int(input("Enter X:"))
y = int(input("Enter Y:"))

if x % y == 0:
    print(f"{x} divided by {y} is {x//y}")
else:
    print("indivisible")
