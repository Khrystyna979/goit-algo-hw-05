commands = """
hello - how can I help you
add [name] [phone] - add new name and phone number
change [name] [phone] - change existing name and phone number
phone [name] - show number of current name
all - show all names and their phones
close or exit - bot shutdown
"""


def parse_input(user_input: str):
    """
    Function for pursing user input
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    """
    Function for error handling
    """
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except ValueError:
            return "You should enter name and phone"
        except KeyError:
            return 'Name not found.'
        except IndexError:
            return 'Please provide name.'

    return inner

@input_error
def add_contact(args, contacts):
    """
    Function for adding information into dict
    """
    name, phone = args
    contacts[name] = int(phone)
    return "Contact added."


@input_error
def change_username_phone(args, contacts):
    """
    Function for changing information into dict
    """
    name, phone = args
    if name in contacts:
        contacts[name] = int(phone)
        return 'Contact updated'
    else:
        return f'Name "{name}" is not defined'
    
@input_error    
def show_phone(args, contacts):
    """
    Function that shows phone of current name
    """
    name = args[0]
    if name in contacts:
        return contacts.get(name)
    else:
        return f'Name "{name}" is not defined'

@input_error      
def show_all(contacts):
    """
    Function that shows all the names and phones
    """

    all_contacts_list = []

    for key, value in contacts.items():
        contact = f'Name is {key}, phone is {value}'
        all_contacts_list.append(contact)

    all_contacts = "\n".join(all_contacts_list)
    return all_contacts



def main():
    contacts = {}
    print("Welcome to the assistant bot!", 'Commands: ', commands, sep='\n')
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == 'change':
                print(change_username_phone(args, contacts))
            elif command == 'phone':
                print(show_phone(args, contacts))
            elif command == 'all':
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except ValueError:
            print('Please choose a command')

if __name__ == "__main__":
    main()
        




