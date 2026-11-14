
import json
import os
import secrets
import string

FILE_NAME = "passwords.json"


def load_passwords():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Error reading password file.")
        return []


def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)


def generate_password(length=12):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        secrets.choice(characters) for _ in range(length)
    )


def add_password(passwords):
    website = input("Enter Website Name: ").strip()
    username = input("Enter Username/Email: ").strip()

    if not website or not username:
        print("Website and username cannot be empty!")
        return

    print("\n1. Enter Password Manually")
    print("2. Generate Strong Password")

    choice = input("Enter Choice: ")

    if choice == "1":
        password = input("Enter Password: ")
    elif choice == "2":
        password = generate_password()
        print("Generated Password:", password)
    else:
        print("Invalid choice!")
        return

    if not password:
        print("Password cannot be empty!")
        return

    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_passwords(passwords)
    print("Password saved successfully!")


def view_passwords(passwords):
    if not passwords:
        print("No passwords saved.")
        return

    print("\n===== SAVED ACCOUNTS =====")

    for account in passwords:
        print("\nWebsite:", account["website"])
        print("Username:", account["username"])
        print("Password:", account["password"])


def search_password(passwords):
    website = input("Enter Website to Search: ").strip().lower()

    found = False

    for account in passwords:
        if website in account["website"].lower():
            print("\nWebsite:", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            found = True

    if not found:
        print("Account not found.")


def delete_password(passwords):
    website = input("Enter Website to Delete: ").strip().lower()

    for index, account in enumerate(passwords):
        if account["website"].lower() == website:
            passwords.pop(index)
            save_passwords(passwords)
            print("Account deleted successfully!")
            return

    print("Account not found.")


def main():
    passwords = load_passwords()

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Generate Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password(passwords)

        elif choice == "2":
            view_passwords(passwords)

        elif choice == "3":
            search_password(passwords)

        elif choice == "4":
            delete_password(passwords)

        elif choice == "5":
            print("Generated Password:", generate_password())

        elif choice == "6":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
