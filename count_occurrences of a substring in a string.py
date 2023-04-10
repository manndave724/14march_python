#count occurrences of a substring in a string.

string=input("enter a string:")
char=input("enter a character:")

count=0
for i in range(len(string)):
    count=count+1

    print("the total numbers of time",char,"has occured=",count)
    