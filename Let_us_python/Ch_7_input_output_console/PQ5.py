line = input("Enter the sentence: ")

characters = len(line)
word = len(line.split())

vowels = 0
digits = 0

for ch in line:
    if ch.lower() in "aeiou":
        vowels+=1
        if ch.isdigit:
            digits+=1

print("number of characters:",characters)
print("number of words:",word) 
print("number of vowels:",vowels)
print("number of digits:",digits)           