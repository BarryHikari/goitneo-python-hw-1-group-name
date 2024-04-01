def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        return "There is no such contact!"

def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "There is no such contact!"

def show_all(contacts):
    if contacts:
        messages = []
        for name, phone in contacts.items():
            message = f"{name}: {phone}"
            messages.append(message)
        return "\n".join(messages)
    else:
        return "The list of contacts is empty!"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))  
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()