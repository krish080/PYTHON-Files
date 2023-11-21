import math
import os
a,b,c=0,0,0
os.system('cls')
a=int(input("Enter the co efficient of x^2 :"))
b=int(input("Enter the co efficient of x :"))
c=int(input("Enter the constant  :"))
d=(b**2)-(4*a*c)
rootOfD=d**0.5
print(rootOfD)

if d>=0:
    if rootOfD.is_integer():
        if ((-b+rootOfD)/(2*a)).is_integer():
            print((-b+rootOfD)/(2*a))
        else:
            print((-b+rootOfD),"/",2*a)
        if ((-b-rootOfD)/(2*a)).is_integer():
            print((-b-rootOfD)/(2*a))
        else:
            print((-b-rootOfD),"/",2*a)

    else:
        print("it is not a perfect square")
elif d==0:
    print(-b/(2*a))

else:
    print("It does not have a root")