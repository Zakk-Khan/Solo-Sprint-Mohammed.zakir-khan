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
        username = input("Enter username: ")
        active_users.append(username)
        print("User added.")

    elif choice == "2":
        print("Active users:", active_users)
        print("Disabled users:", disabled_users)

    elif choice == "3":
        action = input("Type 'disable' or 'enable': ")

        if action == "disable":
            username = input("Enter username: ")
            if username in active_users:
                active_users.remove(username)
                disabled_users.append(username)
                print("User disabled.")
            else:
                print("User not found in active list.")

        elif action == "enable":
            username = input("Enter username: ")
            if username in disabled_users:
                disabled_users.remove(username)
                active_users.append(username)
                print("User enabled.")
            else:
                print("User not found in disabled list.")

    elif choice == "0":
        running = False

    else:
        print("Invalid choice")
    