'''
I)
Let M=6
f(1)=(1-1+41)=41 Prime
f(2)=(4-2+41)=43 Prime
f(3)=(9-3+41)=47 Prime
f(4)=(16-4+41)=53 Prime
f(5)=(25-5+41)=61 Prime
f(6)=(36-6+41)=71 Prime

II)
Problem 1)
Get the value of input x
Square the initial value of x, subtract the initial value of x,and add 41

Problem 2)
From 1 to input M,
pass in values to function f(x) from problem 1
append to list
return list

Problem 3)

For input value of n less than or equal to 1
The value is not prime so return False


For input value greater than 2

If the input value divided by numbers ranged from 1 to upper value of sqrt(N) gives remainder 0
The value is not prime
Else
The value is prime



III)
Let M=4

From 1 to 4, Passing values in f(x)
f(1)=(1-1+41)=41 [41]
f(2)=(4-2+41)=43 [41,43]
f(3)=(9-3+41)=47 [41,43,47]
f(4)=(16-4+41)=53 [41,43,47,53]


Since all values of n is greater than 2,
Dividing 41 by numbers from [1,7] Does not give remainder 0 for any values
Dividing 43 by numbers from [1,7] Does not give remainder 0 for any values
Dividing 47 by numbers from [1,7] Does not give remainder 0 for any values
Dividing 53 by numbers from [1,8] Does not give remainder 0 for any values

Therfore all values are prime



'''





def f(x):
    return x**2-x+41


def build_list(M):
    a=[]
    for i in range(1,M+1):
        ans=f(i)
        a.append(ans)
    return a

def isprime(N):
    if N<=1:
        return False
    for i in range(2,int(N**(1/2))+1):
        if N%i==0:
            return False
    return True

mylist = build_list(4)
for val in mylist:
    if isprime(val):
        print("{0} is prime.".format(val))
    else:
        print("{0} is NOT prime.".format(val))