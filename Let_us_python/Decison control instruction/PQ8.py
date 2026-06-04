import math
C1 = int(input("x coordinate of circle: "))

C2 = int(input("y coordinate of circle: "))
R = int(input("Radius of circle: "))

x = int(input("x coordinate of point: "))
y = int(input("y coordinate of point: "))

distance_from_center = (x-C1)**2 + (y-C2)**2
radius=R**2

if radius<distance_from_center:
    print("Point lies outside the circle.")
elif distance_from_center<radius:
    print("Point lies inside the circle.")
else:
    print("point lies on the circle.")