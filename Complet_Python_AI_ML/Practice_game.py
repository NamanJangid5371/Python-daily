import random
com = random.randint(1,100)
tries = 0 
atempt = 0 

while True:
    atempt = atempt + 1 
    tries = tries + 1
    hum = int(input("guees your number between 1 - 100 :-"))
    print(f"This is your atempt number {atempt}")


    if hum == com:
        print(f"congratulations you have won in {tries} tries!")
        break

    elif hum > com:
        print("sorry wrong guess go lower !")

    elif hum < com:
        print("sorry wrong guess go higher ! ")