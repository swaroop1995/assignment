customer_name=input("customer name:")
units=int(input("units:"))
print("1)industry")
print("2)commercial")
print("3)residence")
option=int(input("select the option:"))
if option==1:
   totalbill=units*5.25
   print("the totalbill is",totalbill)
else:
    if option==2:
        totalbill = units * 4.00
        print("the totalbill is", totalbill)
    else:
        if option==3:
            totalbill = units * 3.08
            print("the totalbill is", totalbill)
        else:
            print("choose the correct option")


