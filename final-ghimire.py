'''
Structured coding process

Let the number of numbers(k) be 3
Let number of experiments(n) be 2

Any random number generated between 0 and 1 
Let n1=0.2
Let n2=0.5
Let n3=0.9

To calculate total minimum average distance:
Sort the values
find the differences
compare differences
find average of these difference over the experiments

Go through the experiment repeateadly 2 or n times

So on first experiment,
Finding distance between n2-n1= 0.5-0.2=0.3
Finding distance between n3-n2= 0.9-0.5=0.4

So the minimum value1=0.3


On 2nd experiment,
Let n1=0.4
Let n2=0.2
Let n3=0.8

Sorting
It becomes n1=0.2 n2=0.4 n3=0.8

Finding distance between n2-n1= 0.4-0.2=0.2
Finding distance between n3-n2= 0.8-0.4=0.4

So the minimum value2=0.2

S0,
The average of minimum values value1 and value2
=(0.2+0.3)/2=0.5/2=0.25




'''





import random



def exp_avg(num_pts,num_experiments):
    i=0
    min_dis=[]
    while(i<num_experiments):
        X = [random.random () for j in range(num_pts)]
        X.sort ()
        least_amt=100000
        for j in range(0,num_pts-1):
            ans=abs(X[j]-X[j+1]) 
            if ans<least_amt:
                least_amt=ans 
        min_dis.append(least_amt)
        
        i=i+1
    
    total=0
    for k in min_dis:
        total=total+k
    return (total/len(min_dis))
    


k = int(input("How many random numbers? (0 to quit): "))





while k>= 2:
    N = int(input(" How many experiments to run? "))
    m = exp_avg(k, N)
    print(" avg. min. distance between numbers = {0}".format(m))
    k = int(input("\nHow many random numbers? (0 to quit): "))
