items = ["food", "tools", "compass"]
def print_items():
    for i in items:
        print("-", i)
def options():
    print("1. add an item")
    print("2. remove an item")
    print("3. view your items")
    print("4. exit the program")

while True:
    options()
    choice = int(input("choose an option by typing a number\n"))
    if choice == 1:
        add = str(input("what do you want to add? (enter only one item)\n"))
        items.append(add)
    elif choice == 2:
        remove = str(input("what item do you want to remove? (enter only one item)\n"))
        items.remove(remove)
    elif choice == 3:
        print_items()
    elif choice == 4:
        break
    else:
        print("please enter a valid option")