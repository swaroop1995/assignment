emp_name=input("enter name:")
salary=float(input("salary:"))
print("1)Manager")
print("2)Analyst")
print("3)Clerk")
option=int(input("select the option:"))
if option==1:
    total_salary=salary+((20/100)*salary)
    print("the total salary is",total_salary)
else:
    if option==2:
        total_salary = salary + ((10/ 100) * salary)
        print("the total salary is", total_salary)
    else:
        if option==3:
            total_salary = salary + ((5 / 100) * salary)
            print("the total salary is", total_salary)
        else:
            print("choose the valid option")

