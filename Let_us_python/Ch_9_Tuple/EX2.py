from datetime import date

date1 = tuple (map(int, input("Enter first date(YYYY MM DD): ").split()))
date2 = tuple (map(int, input("Enter second date(YYYY MM DD): ").split()))

d1 = date(date1[0],date1[1],date1[2])
d2 = date(date2[0],date2[1],date2[2])

days_between = abs((d2-d1).days)

print(days_between)

