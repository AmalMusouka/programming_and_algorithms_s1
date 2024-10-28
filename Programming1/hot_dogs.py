import sys

each_sale = []
max_profit = 0
best_price = 0
for line in sys.stdin:
    each_sale = each_sale + [int(x) for x in line.split()]

each_sale.sort()


for i in range(0, len(each_sale)):
    if i == 0:
        count = [each_sale[i]] * len(each_sale)
        profit = sum(count)
        if profit > max_profit:
            max_profit = profit
            best_price = each_sale[i]

    elif each_sale[i] == each_sale[i - 1]:
        pass
    else:
        count = [each_sale[i]] * len(each_sale[i:])
        profit = sum(count)
        if profit > max_profit:
            max_profit = profit
            best_price = each_sale[i]


print(best_price)
