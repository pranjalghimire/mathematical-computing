#Pranjal Ghimire 1/26/2021
# hw2.py
# This program has many problems, and will NOT run as-is. 
# For part of this assignment, you need to correct it.



#i. The intended purpose of this program is to calculate the quadratic equation to find the roots.

#ii.  Two possible input values:
#  a=1,b=6,c=3            -6+-sqrt(6^2-4*1*3)/2= -6+2sqrt(6)/2 and -6-2sqrt(6)/2
# In this case the expected output is -3+sqrt(6) and -3-sqrt(6)

# a=2,b=4,c=2             -4+-sqrt(4^2-4*2*2)/2*2= -1 
# In this case the expected output is -1 and is the same.

print("Please enter the values of a,b,c to calculate the roots of discriminant.Note that complex numbers are not handled \n")
a = float(input("Please enter value of a \n"))
if a==0:
    print("You cannot divide by zero because it gives ZeroDivisionError: float division by zero\n")

b = float(input("Please enter value of b \n"))
c = float(input("Please enter value of c \n"))

x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)

print("The values of the roots x1 , x2  rounded to 2 decimal places are %.2f, %.2f" %(x1,x2))
