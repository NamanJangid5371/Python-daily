import random
com = random.randint(1,100)
score = 0


while True:

    hum = int(input("Guess your number between 1 - 100 :- "))

    if hum == com:
        print("congratulation you have won !")
        break

    elif hum > com:
        print("Sorry wrong guess go lower.")

    elif hum < com:
        print("Sorry wrong guess go higher.")

    score += 1 
    print(f"number of attempts {score}")
