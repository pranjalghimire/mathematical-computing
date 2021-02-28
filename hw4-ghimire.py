'''
M=a^2+b^2 where a>1 and b>1

I)
let M=17

let a<= rounded down value of sqrt(M) and b<= rounded down value of sqrt(M)
Let a go from 1 to rounded down value of sqrt(M) and then b go from 1 to rounded down value of sqrt(M)

sqrt(17)=4.12       rounded down=4

M= 1^2+1^2 =2
M= 1^2+2^2 =5       
M= 1^2+3^2 =10      
M= 1^2+4^2 =17      

M= 2^2+1^2 =5       
M= 2^2+2^2 =8       
M= 2^2+3^2 =13      
M= 2^2+4^2 =20      

M= 3^2+1^2 =10
M= 3^2+2^2 =13      
M= 3^2+3^2 =18      
M= 3^2+4^2 =25      

M= 4^2+1^2 =17
M= 4^2+2^2 =20      
M= 4^2+3^2 =25      
M= 4^2+4^2 =32      

The possible answers are:
M= 1^2+4^2 =17 and M= 4^2+1^2 =17



II)
Initialize the values of a and b to be 1 and 1 respectively since they are natural numbers
a<-1 b<-1 

Let count of the solutions be zero.
count <- 0

Let sqrt(M) rounded down be the maximum values of a and b
max<-sqrt(M)  rounded down


1)For each value of a check if the value of b satisfies the condition  M=a^2+b^2 
  If condition is satisfied, increase the count size 


2)Increase the value of b and go back to step 1 until b=max 

3)Reset the value of b to 1

4)Increase the value of a and refollow the steps until a=max



III)
Let M=11

Setting value of a and b to 1.
Setting count to zero.

Max values of a and b =sqrt(11)= 3.31 Rounded down =3
Therefore max=3

Start the steps
a^2+b^2 =1^2+1^2=1
a^2+b^2 =1^2+2^2=5
a^2+b^2 =1^2+3^2=10

No values of m are found so count is 0

Resetting value of b to 1 since b=max

Increasing the value of a by 1,

a^2+b^2 =2^2+1^2=5
a^2+b^2 =2^2+2^2=8
a^2+b^2 =2^2+3^2=13

No values of m are found so count is 0

Resetting value of b to 1 since b=max

Increasing the value of a by 1,

a^2+b^2 =3^2+1^2=10
a^2+b^2 =3^2+2^2=13
a^2+b^2 =3^2+3^2=18

No values of m are found so count is 0

Resetting value of b to 1 since b=max

Since we reached a=max,we finish our condition

The value of count is 0, so there are no solutions for this value

'''


import math
n=1

def sum_of_squares(n):
    count=0
    for a in range(1 ,math.ceil(n**(1/2))):
        for b in range(1 ,math.ceil(n**(1/2))):
            if a**2 + b**2 == n:
                count+=1
                print("{0}∗∗2 + {1}∗∗2 = {2}.".format(a,b,n))
    return count

while n >= 1:
    n = int(input("Enter a positive integer n: "))
    numsq = sum_of_squares(n)
    print("{0} can be written as a sum of squares in {1} ways.".format(n, numsq ))


                