'''
I)
Let N=6 a=[]
a=[6] F3n1(6)
Since even, n//2= 6//2 =3    a=[6,3]    F3n1(3)
Since odd, 3*n+1= 3*3+1 =10  a=[6,3,10] F3n1(10)
Since even, n//2= 10//2 =5   a=[6,3,10,5] F3n1(5)
Since odd, 3*n+1= 3*5+1 =16  a=[6,3,10,5,16] F3n1(16)
Since even, n//2= 16//2 =8   a=[6,3,10,5,16,8] F3n1(8)
Since even, n//2= 8//2 =4   a=[6,3,10,5,16,8,4] F3n1(4)
Since even, n//2= 4//2 =2   a=[6,3,10,5,16,8,4,2] F3n1(2)
Since even, n//2= 2//2 =1   a=[6,3,10,5,16,8,4,2,1] 




II)
Let n be the input for the sequence
Add the input n to the list.
If n=1, it is the terminating condition

Otherwise,
1)If n is even, compute n//2 and add to list as well as check terminating condition
2)If n is odd, compute 3*n+1 and add to list as well as check terminating condition
3)If terminating condition n=1 is satisfied add to the list and finish

Check if steps 1,2 fit the description and end once step 3 is satisfied





III)
Let n=5
Adding to the list,[5]
Since not terminating condition,

As step 2 is satisfied if odd, compute 3*n+1=16 
Adding to list, [5,16]
Since terminating condition is not satisfied we repeat the steps.

As step 1 is satisfied if even, compute n//2=8 
Adding to list, [5,16,8]
Since terminating condition is not satisfied we repeat the steps.

As step 1 is satisfied if even, compute n//2=4 
Adding to list, [5,16,8,4]
Since terminating condition is not satisfied we repeat the steps.

As step 1 is satisfied if even, compute n//2=2 
Adding to list, [5,16,8,4,2]
Since terminating condition is not satisfied we repeat the steps.

As step 1 is satisfied if even, compute n//2=1 
Adding to list, [5,16,8,4,2,1]
Since terminating condition is not satisfied, we are done with the solution.

'''




def F3n1(n):
    if n%2!=0:
        return 3*n+1
    return n//2

def sequence(n):
    a=list()
    while True:
        a.append(n)
        if n==1:
            break
        n=F3n1(n)
      
    return a    
    
N = int(input("Enter a positive integer N:"))
seq = sequence(N)
print("The resulting sequence is: {0}".format(seq ))
print("It has length {0}".format(len(seq )))
