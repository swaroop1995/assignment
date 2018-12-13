m1=int(input("m1:"))
m2=int(input("m2:"))
m3=int(input("m3:"))
m4=int(input("m4:"))
m5=int(input("m5:"))
m6=int(input("m6:"))
totalmarks=m1+m2+m3+m4+m5+m6
if totalmarks>360:
    print("first class")
else:
    if totalmarks>=300 and totalmarks<360:
        print("second class")
    else:
        print("third class")