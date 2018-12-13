print("1)The parrot is talking")
print("2)the parrot is not talking")
option=int(input("select the option:"))
hour=int(input("hour:"))
if option==1 and (hour<7 or hour>20):
    print("we are in trouble")
else:
    print("we are not in trouble")
