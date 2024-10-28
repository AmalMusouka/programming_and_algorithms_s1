import sys

each_sale = []
max_profit = 0
best_price = 0
for line in sys.stdin:
    each_sale = each_sale + [int(x) for x in line.split()]

each_sale.sort()

unique_prices = []
for price in each_sale:
    if price not in unique_prices:
        unique_prices.append(price)


for price in unique_prices:
    total_sold_at_price = [i for i in each_sale if i >= price]
    each_profit = [price] * len(total_sold_at_price)
    profit = sum(each_profit)
    if profit > max_profit:
        max_profit = profit
        best_price = price

print(best_price)
