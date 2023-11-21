print("1.SQUARE")
print("2.RECTANGLE")
print("3.CIRCLE")
print("4.CUBE")
print("5.CUBOID")
print("6.SPHERE")
choice=int(input("ENTER YOUR CHOICE:"))
if(choice==1):
    s=int(input("ENTER THE VALUE OF SIDE:"))
    area=s**2
    print("THE AREA OF SQUARE IS:",area)
elif(choice==2):
    l=int(input("ENTER THE LENGTH:"))
    b=int(input("ENTER THE WIDTH:"))
    area=l*b
    print("THE AREA OF RECTANGLE IS:",area)
elif(choice==3):
    r=int(input("ENTER THE RADIUS:"))
    area=3.14*r**2
    print("THE AREA OF CIRLCLE IS:",area)
elif(choice==4):
    s=int(input("ENTER THE VALUE OF SIDE:"))
    lsa=4*s**2
    tsa=6*s**2
    print("THE LATERAL SURFACE AREA OF CUBE IS:",lsa)
    print("THE TOTAL SURFACE AREA OF CUBE IS:",tsa)
elif(choice==5):
    l=int(input("ENTER THE LENGTH:"))
    b=int(input("ENTER THE WIDTH:"))
    h=int(input("ENTER THE HEIGHT:"))
    tsa=2*l*b+2*b*h+2*h*l
    print("THE TOTAL SURFACE AREA OF CUBOID IS:",tsa)
elif(choice==6):
    r=int(input("ENTER THE RADIUS:"))
    area=4*3.14*r**3
    print("THE AREA OF SPHERE IS:",area)
else:
    print("PLEASE ENTER A VALID INPUT")