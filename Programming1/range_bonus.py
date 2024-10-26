starting_year = int(input())
final_year = int(input())

days = 0
current_year = starting_year

starting_year % 4
if (
    current_year % 4 == 0
    and current_year % 100 != 0
    or (current_year % 100 == 0 and current_year % 400 == 0)
):
    days += 366
else:
    days += 365
current_year += 1
print(days)
