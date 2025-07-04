'''9.Write a Python program to check if a triangle is equilateral, isosceles or 
scalene. 
 
    Note : 
 
    An equilateral triangle is a triangle in which all three sides are equal. 
    A scalene triangle is a triangle that has three unequal sides. 
    An isosceles triangle is a triangle with (at least) two equal sides.'''

# To get the user input for the angles of the triangle
print('Enter the 3 angles of a triangle: ')
angle_1 =int(input("1. first angle: "))
angle_2 =int(input("2. second angle: "))
angle_3 =int(input("3. third angle: "))

if angle_1 + angle_2 + angle_3 ==180: # because the sum of the angles in any triangle is 180
    if angle_1==angle_2 and angle_2==angle_3 and angle_3==angle_1:
        print('The triangle is an Equilateral traingle')
    elif angle_1==angle_2 or angle_1==angle_3 or angle_1==angle_1:
        print('It is an Isosceles traingle')
    else:
        print('It is a Scalene triangle')
else:
    print('No triangle suits the description')