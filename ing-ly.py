mystr=input("enter a string:-")

if len(mystr)<3:
    print("unchnaged",mystr)

if mystr.endswith('ing'):
    mystr+='ly'

elif len(mystr)>=3:
    mystr+='ing'
print(mystr)
