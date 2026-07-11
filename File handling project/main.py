from pathlib import Path
import os


def createfile():
    try:
        name = input("Tell your file name:-")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("What you want to write:-")
                fs.write(data)
                print("Erro file name is alredy exists.")
        else:
            print("Error file created successfully.")

    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        name = input("Please tell your file name :-")
        path = Path(name)
        if path.exists:
            with open(path,"r") as fs:
                content = fs.read()
                print(f"your file content is \n {content}")
        else:
            print("error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")



def updatefile():
    name = input("Please tell your file name :- ")
    path = Path(name)

    if path.exists():
        print("operations ")
        print("1 . Renaming the file ")
        print("2 . Appending the content")
        print("3 . Overwirting the file")
        
    if path.exists: 
        with open(path,"r") as fs:
            content = fs.read()
            print(f"change the file name to this:{}")
def deletfile():
    pass


print("press 1 for creating a file.")
print("press 2 for reading a file.")
print("press 3 for updating a file.")
print("press 4 for deleting a file.")

a = int(input("\ntell your response :- "))

if a == 1: 
    createfile()
if a == 2: 
    readfile()
if a == 3: 
    updatefile()
if a == 4: 
    deletfile()

