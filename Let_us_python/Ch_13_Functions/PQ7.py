def compute(n):
    sumc = n + (n*10+n) + (n*100+n*10+n) + (n*1000+n*100+n*10+n)
    return sumc

print(compute(4))
print(compute(7))