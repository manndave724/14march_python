# Write a python program to get the fibonacci series of given range

n=int(input("Enter a number : "))
n1=0
n2=1
print("fibonacci sequence :",n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
    