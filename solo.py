import csv

ACTIVE_FILE = "active_users.csv"
DISABLED_FILE = "disabled_users.csv"



# LOAD USERS FROM FILE

def load_users(filename):
    users = []
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(row[0])
    except FileNotFoundError:
        pass
    return users



# SAVE USERS TO FILE

def save_users(filename, users):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for user in users:
            writer.writerow([user])



# MENU

def display_menu():
    print("\n1. Add User")
    print("2. View active/disabled Users")
    print("3. Enable/Disable Users")
    print("0. Exit")



# LOAD DATA AT START

active_users = load_users(ACTIVE_FILE)
disabled_users = load_users(DISABLED_FILE)

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
        save_users(ACTIVE_FILE, active_users)
        save_users(DISABLED_FILE, disabled_users)
        print("Data saved. Exiting app.")
        running = False

    else:
        print("Invalid choice")