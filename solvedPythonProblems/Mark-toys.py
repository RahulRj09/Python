a = input()
a = a.split()
for i in range(2):
    a[i] = int(a[i])
toys = a[0]
money = a[-1]
prices = input()
prices = prices.split()
for i in range(toys):
    prices[i] = int(prices[i])
total = 0
b = []
for price in prices:
    if price <= money:
        b.append(price)
b = sorted(b)
for price in b:
    if money % price < money:
        total = total + 1
        money = money - price
print(total)
