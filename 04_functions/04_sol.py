# def circle(r):
#     area = 3.14 * r * r
#     circumference = 2 * 3.14 * r

#     print("area = ", area , "\n")
#     print("circumference = ", circumference,)


# circle(7)

# method 2

import math

def circle_info(r):
    area = math.pi * r **2
    circm = 2 * math.pi * r

    return area, circm

a , c = circle_info(7)   
a1 = round(a,2)            #for precision up to 2 decimal places
c1 = round(c,2)

print( "area : ", a1, "  circumference: ", c1)


