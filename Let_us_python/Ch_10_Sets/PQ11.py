import random

numbers = set()

while len(numbers)<10:
    numbers.add(random.randint(15,45))

print("Original Set:")
print(numbers)

count=0
for num in numbers:
    if num < 30:
        count += 1

print("Numbers less then 30:",count)

for num in list(numbers):
    if num > 35:
        numbers.remove(num)

print("Numbers after removing number greater than 35:")
print(numbers)