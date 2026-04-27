active_users = []
disabled_users = []

def display_menu():
    print("1. Add User")
    print("2. View active/disabled Users")
    print("3. Enable/Disable Users")
    print("0. Exit")

running = True

while running:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        print("Input Username")
    elif choice == "2":
        print(active_users + disabled_users)
    elif choice == "3":
        print("input username to disable")
    elif choice == "0":
        running = False
    else:
        print("Invalid choice")