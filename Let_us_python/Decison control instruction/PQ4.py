Rage = int(input("Enter the age of Ram: "))
Sage = int(input("Enter the age of Shyam: "))
Aage = int(input("Enter the age of Ajay: "))

if Rage>Aage and Sage>Aage:
    print("Ajay is youngest.")
elif Sage>Rage and Aage>Rage:
    print("Ram is youngest.")
elif Aage>Sage and Rage>Sage:
    print("Sage is youngest.")
else:
    print("They are both same age.")