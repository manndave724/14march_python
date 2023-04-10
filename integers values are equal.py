#Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5.

a=int(input("enter the value of a :- "))
b=int(input("enter the value of b :- "))

if a==b or a+b==5 or a-b==5 or b-a==5:
    print(True)

else:
    print(False)

