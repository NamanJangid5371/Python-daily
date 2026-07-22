# class Car:
#     a = 12 #atribute

#     def hello(): #method
#         print("How are you")

# print(Car.a) #accessing the class.

# Car.hello

# class bags:
#     name = "NotYourCollege"

#     def details():
#         print("hello this ia a country who creates bag")

# reebok = bags()
# campus = bags()

# print(reebok.details)

# class bags:
#     def __init__(self,material,zips,pockets): #__init__ functions calls automatic when ever the class is called.
#         self.material = material  #to target the object location we use self keyword.
#         self.zips = zips          #
#         self.pockets = pockets 
    
# reebok = bags("leather",3,2)
# campus = bags("polyster",2,4)

# print(reebok.zips)
# print(campus.material)    

# class Animal:
#     a = 12 #class attribute 

#     def __init__(self,name):
#         self.name = name # object/instance atribute       


#     def hello(self): #instance/object method captures the location of object.
#         print(f"how are you my name is {self.name}")

#     @classmethod #class method. caputer the location of class
#     def detail(cls):
#         print("how are you.")

#     @staticmethod
#     def speak():
#         print("hello how are you I am a static method")


# obj = Animal("Lion")

# obj.hello()

#============================================================================================================================================================================

# Inheritance
# class animal:
#     a = 12
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#             print(f"Hello my name is {self.name}")
    
# class human(animal):
#     pass

# obj = animal("lion")
# obj2 = human("harsh")

# obj2.details()
# print(obj2.a)
# ==========================================================================================================================================================================

# class BagFactory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def details(self):
#         print("your bag details are :")
#         print(self.material)
#         print(self.zips)
#         print(self.pockets)

# class reebok(BagFactory):
#     def __init__(self, material, zips, pockets,color):
#         super().__init__(material, zips, pockets)
#         self.color = color

#     def details(self):
#         print(self.color)
#         return super().details()

# bag1 = BagFactory("leather",3,4)
# bag2 = reebok("polyster",4,2)

#===================================================================================================================================================================================
# Multi level inheritance

# class animals:
#     def __init__(self,name):
#         self.name = name

# class humans:
#     def __init__(self,id):
#         self.id = id

# class robots(animals,humans):
#     def __init__(self, name, id):
#         humans.__init__(id)
#         animals.__init__(name)

# robo = robots(12,"Naman")

#===================================================================================================================================================================================

# Polymorphisem

# class animal:
#     def speak(self):
#         print("Animals will not speak.")

# class humans:
#     def speak(self):
#         print("We are humans we can speak.")

# obj = animal()
# obj2 = humans()

# obj.speak()
# obj2.speak()

# Method overriding

# class animal:
#     a = 12 
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(f"your name is {self.name}")

# class Humans(animal):
#     b = 12

#     def details(self):
#         super().details()
#         print(f"your info is {self.name} and this is all we have.")

# obj = Humans("Harsh")
# print(obj.a)
# obj.details()

#when we are doing inheritance and parent and child classes
#have same method name so the child class method will overrider your parent class method.

#Method overloading 

# class hello:
#     def speak(self,a):
#         print(f"how are you ")

#     def speak(self,a,b):
#         print("how are you 1")


#=============================================================================================================================================

#Enclapsulation

# class factory:
#     __name = "KIA" #public class attribute
#     _old = 12  # Protected class attribute
    
#     def __init__(self,colour,tyre,type):
#         self.colour = colour  #public object attribute 
#         self.tyre = tyre
#         self.type = type

#     def detail(self): #public method
#         print("hello your details are: ")

# obj = factory("Silver","MRF","Compact SUV")
# class hello(factory):
#     print(factory.__name)
# obj.name = "Honda"
# print(obj.name)
# obj._old = 13
# print(obj._old)

#=============================================================================================================================================================================

# class hello:
#     __a = 12

#     @classmethod
#     def info(cls):
#         print(cls.__a)

# obj = hello()
# obj.info
# print(obj.__a)

#=========================================================================================================================================================================

#Abstraction 

# from abc import ABC, abstractmethod

# class enforce(ABC):
#     @abstractmethod
#     def enginestart():
#         pass
    

# class car(enforce):
#     def enginestart():
#         pass

# class bike(enforce):
#     def enginestart():
#         pass

# class truck(enforce):
#     def enginestart():
#         pass

# obj1 = bike()
# obj2 = car()
# obj3 = truck()

#============================================================================================================================================================================

#Dunder methods
# class Animal:
#     def __init__(self,name):
#         self.name = name 
    
#     def __str__(self):
#         return f"Hello my name is {self.name}"
# obj = Animal("Lion")

# print(obj)

# class numbers:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,other):
#         return self.num + other.num

# num1 = numbers(20)
# num2 = numbers(30)

# print(num1 + num2)
        
