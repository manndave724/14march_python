#sum of three given integers.
#However if two values are equal sum will be zero.

a = int(input("enter value 1 : "))
b = int(input("entr value 2 : "))
c = int(input("enter value 3 : "))

if a == b or b == c or c == a:
    print(f"sum is : 0")

else:
    d = a + b + c
    print(f"sum is : {d}")


