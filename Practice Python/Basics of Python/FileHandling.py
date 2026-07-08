# open("hello.txt","x") #create a new file 

# file = open("New.txt","w")

# data = input("Waht you want to wirte in the file :- ")

# file.write(data)

# file = open("number_Guss_game.py","r")
# print(file.read())

with open("New.txt","a") as f:
    f.write(" " + "i want to see if it is working or not")