'''

I) u(n)=(u(n-1)+(C/u(n-1)))/2 where n>=1
Let C=5 N=6
u(0)=1
u(1)=(u(1-1)+(5/u(1-1)))/2      =(u(0)+(5/u(0))))/2       =(1+(5/1))/2   =3
u(2)=(u(2-1)+(5/u(2-1)))/2      =(u(1)+(5/u(1))))/2       =(3+(5/3))/2   =7/3 =2.333333333
u(3)=(u(3-1)+(5/u(3-1)))/2      =(u(2)+(5/u(2))))/2       =(7/3+(5/(7/3)))/2   =47/21 =2.238095238
u(4)=(u(4-1)+(5/u(4-1)))/2      =(u(3)+(5/u(3))))/2       =(47/21+(5/(47/21)))/2   =2207/987 =2.236068896
u(5)=(u(5-1)+(5/u(5-1)))/2      =(u(4)+(5/u(4))))/2       =(2207/987+(5/(2207/987)))/2   =2207/987 =2.236067977
u(6)=(u(6-1)+(5/u(6-1)))/2      =(u(5)+(5/u(5))))/2       =(2207/987+(5/(2207/987)))/2   =2207/987 =2.236067977

After u(5),
u(n)=2207/987 =2.236067977 =sqrt(C)


II)
Set n <- 0, u(n) <-1
Let C <- Greater than 1 ,u(n)<- (u(n-1)+(C/u(n-1)))/2

Keep doing this until n=N or n=Sqrt(C):
n<- n+1,

Put the previous value of u(n) function into current u(n-1) function
u(n-1) <- u(n)


The value of u(n) is u(n-1) if u(n)=sqrt(C) 

Else
u(n)<- (u(n-1)+(C/u(n-1)))/2


III)
Set n=0, u(n)=1
Let c=2,u(n)<- (u(n-1)+(C/u(n-1)))/2
Let N=6

If n=1,
u(1)= (u(0)+(C/u(0)))/2     =(1+2/1)/2  =1.5
u(2)= (1.5+(2/1.5))/2      =1.416666667
u(3)= (1.416666667+(2/1.416666667))/2   =1.414215686
u(4)= (1.414215686+(2/1.414215686))/2   =1.414213562
u(5)= (1.414213562+(2/1.414213562))/2  =1.414213562

As we can see, we have found that n+sqrt(C) so we do not need to code for n=N



'''
C=float(input("Please enter a floating number C greater than equal to 1. \n"))
N=int(input("Please enter a positive value N \n" ))
u=1


if N==0:
    print("The value of u is %.8f \n",u)
else:
    for i in range(1,N+1):
        if u==0:
            print("Division by zero error")
        if u==(C**(1/2)):
            print("The sqrt N value has been found")
            break
        u=((u+(C/u))/2)
    print(" The value of u is %.8f \n"%u)