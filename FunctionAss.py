# Write a fuction that calculates the area of a circle, use the return function

#import math

def Area_circle():
    pi = 3.142

    radius= float(input('Enter the radius of the circle: '))

    area = pi *radius**2

    return area

output = Area_circle()
print(f'The area of the circle is {output}')

    


