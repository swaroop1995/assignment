print("1)Yes,it is a weekday")
print("2)No,it is not a weekday")
print("3)yes,it is a vacation")
print("4)No,it is not a vacation")
weekday=int(input("enter option:"))
vacation=int(input("enter option:"))
if weekday==2 and vacation==4:
    print("true")
else:
    if weekday==1 and vacation==4:
        print("false")
    else:
        if weekday==2 and vacation==3:
            print("true")