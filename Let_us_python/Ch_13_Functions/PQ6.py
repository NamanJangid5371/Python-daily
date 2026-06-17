def count_lower_upper(s):
    count = {
        "Lowercase": 0,
        "Uppercase": 0
    }

    for char in s:
        if char.isupper():
            count["Uppercase"] += 1
        elif char.islower():
            count["Lowercase"] += 1

    return count

s1 = "Hello World"
s2 = "Python Programing"
s3 = "OpenAI GPT"

print(count_lower_upper(s1))
print(count_lower_upper(s2))
print(count_lower_upper(s3))


