'''
I)Let x0=2
Let f(x)=x**2-3
Then d(x)=2*t

Computing using x(n+1)=x(n)-(f(x0)/d(x))
x1=2-(1/4)=1.75
x2=1.75-(0.0625/3.5)=1.7321
x3=1.7321-(1.7041e(-4)/3.4642)=1.732050808
x4=1.732050808-(2.41982e(-9)/3.464101617)=1.732050808

Since values are equal the output is x is 1.732050808

II)
Let x0=n
Choose a function
Find the derivative of function d(x)

Find the next value of x iteratively using x(n+1)=x(n)-(h(x)/d(x))
    If absolute value of  f(x(n))/h(x) is less than the tolerance value return x
    If absolute value of derivative d(x) is less than the tolerance value return error
If after 20 iterations then the value did not converge and return error


III)
Let n=2
Let x(0)=-2
Let h(x)=x^5+x^4+x^2-2x+1
Then d(x)=5x^4+4x^3+2x-2
Let tolerance value be 1*10**-10

x(1)=-2-(-7/42)= -1.83333
x(2)=-1.83333-((-1.386)/(33917/1296))= -1.78035
x(3)=-1.78-(-0.1096/22.0747)= -1.775392586
x(4)=-1.7754-(-8.9*10**-4/21.74085)=-1.7753514637
x(5)=-1.77535146-(-6.095*10**-8/21.73804)=-1.7753514609
x(6)=-1.7753514609-(-2*10**-16/21.73797)=-1.7753514609
Since h(x) is less than tolerance value the answer returned is x=-1.7753514609

Less than 20 iterations


                            

'''
import math

#works for oscillating sequence but only outputs one root instead of multiple roots
def Newton(Function, Derivative, x0, epsilon):
    x_curr=x0
    for i in range(0,20):
            
            fun=Function(x_curr)
            dev=Derivative(x_curr)
            
            #if y-value is near 0
            if epsilon>abs(fun):
                return x_curr
            
            #if value is close to 0 slope
            if epsilon>abs(dev):
                print("Error really close to zero slope") 
                return
            
            x_next=x_curr-(fun/dev)
            x_curr=x_next
        
    print("Failture to converge") 
    return

'''

x = 2

def g1(t):
    return t**2-3

def dg1(t):
    return 2*t

if type(xn) is float:
    print("g1(%1.8f) = %1.25f" % (xn , g1(xn)))
        
xn = Newton(g1 , dg1 , x, 1e-10)

'''

x2=-1.5


def g2(t):
    return t**5+t**4+t**2-2*t+1

def dg2(t):
    return 5*t**4+4*t**3+2*t-2


xn2=Newton(g2,dg2,x2,1e-10)


    
if type(xn2) is float:
   print("The equation is g2(%1.8f) = %1.25f" % (xn2 , g2(xn2)))






x3=-1

def g3(t):
    return t**3-math.cos(2*t)

def dg3(t):
    return 3*t**2+2*math.sin(2*t)

xn3=Newton(g3,dg3,x3,1e-10)


    
if type(xn3) is float:
   print("The equation is g3(%1.8f) = %1.25f" % (xn3 , g3(xn3)))