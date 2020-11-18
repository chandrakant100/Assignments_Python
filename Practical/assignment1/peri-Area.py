import math

diameter = input("Enter the diameter of the circle: ")

if diameter.isnumeric() == False:
    print("Input is not numeric!!!")
    exit()

diameter = float(diameter)
radius = diameter / 2

Area = math.pi * radius * radius
perimeter = math.pi * diameter

print("The Area of the circle is %.2f and the perimeter is %.2f"%(Area,perimeter))



