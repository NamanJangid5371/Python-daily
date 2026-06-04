s1 = int(input("Enter the side 1 of triangle: "))
s2 = int(input("Etner the sied 2 of triangle: "))
s3 = int(input("Enter the sied 3 of triangle: "))


if  s1==s2==s3:
    print("Trinagle is eqilateral.")
elif s1==s2 or s1==s3 or s3==s2:
    print("Triangle is isoscalene.")
elif s1**2==s2**2+s3**2 or s2**2==s1**2+s3**2 or s3**2==s1**2+s2**2:
    print("Triangle is right angle triangle.")
else:
    print("Triangle is scalen.")
