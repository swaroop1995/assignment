no1=int(input("no1:"))
no2=int(input("no2:"))
no3=int(input("no3:"))
if no1>no2 and no1>no3:
    print(no1,"is the buggest")
else:
    if no2>no1 and no2>no3:
        print(no2,"is biggest")
    else:
        print(no3,"is biggest")
