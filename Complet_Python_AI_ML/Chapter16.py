a = int(input("Please tell your number 1: "))
b = int(input("Please tell your number 2: "))
try:    
    print(a/b)
except Exception as err:
    print(f"Sorry and error acured as {err}")
else:
    print("No error accured.")
finally:
    print("There are error or there are no errors I will run no matter what.")

name = input("tell your name:-")
print(f"Your name is {name}") 

age = int(input("Enter your age: "))
if age < 18:
    raise TypeError("Your are not eligible: ")

print("Your are eligible.")