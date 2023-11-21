import os
from datetime import date
from datetime import datetime

#getting the no of items
noOfItem=int(input("Enter the no of items: "))

#init variables
itemName,itemPrice,itemQuantity,itemTotal=[],[],[],[]

#getting date and time

dt=datetime.now()
dt=str(dt)
dt=dt.split()

#getting the item name price and quantity
for i in range(noOfItem):
    os.system('cls')
    itemName.append(input("Enter the name of item no "+str(i+1)+": "))
    os.system('cls')
    itemPrice.append(int(input("Enter the price of item no "+str(i+1)+": ")))
    os.system('cls')
    itemQuantity.append(int(input("Enter the quantity of item no "+str(i+1)+": ")))
    os.system('cls')
    itemTotal.append(itemPrice[i]*itemQuantity[i])

#printing the bill
print(f"{'Welcome to Target': ^42}")
print("------------------------------------------")
print("Date :"+str(dt[0]))
print("Time :"+str(dt[1]))
print("------------------------------------------")
print("Name         Price       Qty       Total  ")
print(" ")

for i in range(noOfItem):
    print(f"{str(itemName[i]): <12}",f"{str(itemPrice[i]): <11}",f"{str(itemQuantity[i]): <9}",f"{str(itemTotal[i]): <10}")

#finding the total amount
tot=0
for i in itemTotal:
    tot+=i
#calculating tax
gst=(tot/100)*2.5
cgst=(tot/100)*6

print("------------------------------------------")
print(f"{'Total:'+str(tot): >42}")
print("------------------------------------------")

tot+=gst
tot+=cgst

#printing tax and total amount
print("------------------------------------------")
print(f"{'GST:'+str(gst): >42}")
print(f"{'CGST:'+str(cgst): >42}")
print("------------------------------------------")
print(f"{'Total:'+str(tot): >42}")
print("------------------------------------------")
