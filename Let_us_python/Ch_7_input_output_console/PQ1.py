unit = float(input("Enter the Unit consummed: "))

if unit<100:
    f1 = unit*5
    print(f"Total bill: {f1}")
elif unit<200:
    f2 = 100*5+(unit-100)*7
    print(f"Total bill: {f2}")
elif unit>=200:
    f3 = 100*5+100*7+(unit-200)*10
    print(f"Total bill: {f3}")