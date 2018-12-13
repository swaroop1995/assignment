print("1)Monkey A and B are smiling")
print("2)Monkey A and B are not smiling")
print("3)Monkey A is smiling")
print("4)Monkey B is not smiling")
option=int(input("select the option:"))
if option==1 or option==2:
    print("we are in trouble")
else:
    if option==3 or option==4:
        print("we are not in trouble")
