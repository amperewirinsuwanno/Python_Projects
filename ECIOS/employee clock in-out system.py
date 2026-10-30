# this is a system which employees (of any company) enter their names to clock in or out & anyone can view the currently clocked-in employees. anyone can clock in or out using SOMEONE ELSE'S name. i don't know how to fix that problem.

clocked_in = []
def options():
    print("1. clock in an employee")
    print("2. clock out an employee")
    print("3. view clocked in employees")
    print("4. exit the system")
    print("5. explain an option")

while True:
    print("")
    options()
    choice = int(input("choose an option by typing a number.\n"))
    if choice == 1:
        clock_in = str(input("enter an employee's name.\n"))
        clocked_in.append(clock_in)
    elif choice == 2:
        clock_out = str(input("enter an employee's name.\n"))
        clocked_in.remove(clock_out)
    elif choice == 3:
        print("currently clocked in employees:")
        for i in clocked_in:
            print("-", i)
    elif choice == 4:
        confirm_exit = str(input("are you sure you want to exit? y/n\n"))
        if confirm_exit == "y":
            break
        if confirm_exit == "n":
            continue
    elif choice == 5:
        explain = int(input("choose an option to explain by typing the number.\n"))
        if explain == 1:
            print("explanation: clock in an employee for work. result is kept inside this device/code.")
        elif explain == 2:
            print("explanation: clock out an employee for work. result is kept inside this device/code.")
        elif explain == 3:
            print("explanation: view currently clocked in employees. clocked out employees will not appear in this list.")
        elif explain == 4:
            print("explanation: exit the employee clock in-out system.")
        elif explain == 5:
            print("explanation: the system explains an option.")
        else:
            print("please enter a valid option.")
    else:
        print("please enter a valid option.")
