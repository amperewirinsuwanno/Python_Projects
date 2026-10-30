# made with a little bit of help from AI

to_dos = []
def options():
    print("to-do list options")
    print("1. add a to-do")
    print("2. check a to-do")
    print("3. view to-dos")
    print("4. exit")
def not_valid():
    print("please enter a valid option.")

while True:
    print("")
    options()
    choice = int(input("choose an option by entering a number.\n"))
    if choice == 1:
        add = str(input("enter a to-do.\n"))
        to_dos.append(add)
    elif choice == 2:
        check = int(input("enter a to-do (number) to check.\n"))
        to_dos.pop(check - 1)
    elif choice == 3:
        print("")
        for i in range(len(to_dos)):
            print(i + 1, ":", to_dos[i])
        if len(to_dos) == 0:
            print("there are no to-dos.")
    elif choice == 4:
        confirm_exit = str(input("are you sure you want to exit? y/n\n"))
        if confirm_exit == "y":
            break
        elif confirm_exit == "n":
            continue
        else:
            not_valid()
    else:
        not_valid()