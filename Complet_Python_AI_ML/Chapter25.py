# Decorators
# def extragreeting(func):
#     def wrapper():
#         print("hello from the Appinop.")
#         func()
#         print("thankyou visit again.")

#     return wrapper
    

# @extragreeting
# def greeting():
#     print("good morning")

# greeting()
#====================================================================================================
# Argument
# def addition(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s

# print(addition(20,30,79,89,54,23,45,78,90,89))
#===========================================================================================================
# Key word argument

# def info(**kwargs):
#     return kwargs

# info(name = "Akarsh" ,age = 21 ,profession = "Data Scientist")

# def extragreeting(func):
#     def wrapper(*args,**kwargs):
#         print("hello from the Appinop.")
#         func(*args,**kwargs)
#         print("thankyou visit again.")

#     return wrapper

# @extragreeting
# def addition(a,b,c):
#     print(a + b + c)
    
# addition(10,20,30)
#====================================================================================================

# a = 20
# if a % 2==0:
#     print("even numbers")
# else:
#     print("odd numbers")

# print("even number") if a % 2 == 0 else print("odd number") ternary operation
#===============================================================================================================

#comprehension one liner

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# b = [i for i in a if i % 2 == 0]


# print(b)

#================================================================================================================

# def check(a):
#     if a % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")

# check(12)

## lambda function
# check = lambda x: print("even number") if x % 2 == 0 else print("odd number")
# check(12)
#==================================================================================================================

#Map function 

# a = ["Naman","Lokesh","Sarthak","Rajyavardhan"]

# lengths = list(map(len,a))

# print(lengths)

#======================================================================================================================

# Map and lambda function

# temp_cel = [0,20,30,35]

# def converter(a):
#     far = (a* 9/5) +32
#     return far

# temp_far = list(map(lambda x : (x * 9/5) + 32, temp_cel))
# print(temp_far) 

#=======================================================================================================================

# Filter function
# m = [35,80,80,12,60,49]

# passed = list(filter(lambda x : x >= 40,m))

# print(passed)

#======================================================================================================================================

#Zip funcition
name = ["Naman","Kushal","Harsh","Mannu"]
marks = [90,90,98,99]

result = list(zip(name,marks))

print(result)

