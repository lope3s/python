from collections import namedtuple


options = {
    "1": "Add new contact",
    "2": "Search contact",
    "3": "Show phonebook",
    "4": "Exit"
}


def get_contacts_data():
    name = input('Please provide the contact name: ')
    phone = input('Please provide the contact number: ')

    return (name, phone)


def get_action():
    print("Select one of the following options:")
    for key in options:
        print(f'{key}) {options[key]}')

    selected_action = ''

    while selected_action not in options:
        selected_action = input('\nYour choice: ')

    return int(selected_action)


def store_contact(agenda, contact_data):
    ContactData = namedtuple('ContactData', ['name', 'phone_number'])

    # Here we're using the unpacking operator (*) to spread all the elements
    # from our contact_data into our namedtuple ContactData.
    # Note that the number of elements in contact_data need to be EXACTLY the
    # same as the number of arguments, otherwise a TypeError will be raised.
    named_contact = ContactData(*contact_data)

    agenda.append(named_contact)


if __name__ == "__main__":
    run = True

    phonebook = []

    while run:
        action = get_action()

        if action == 4:
            run = False
            print("Bye!")
            continue

        if action == 1:
            contact_data = get_contacts_data()
            store_contact(phonebook, contact_data)

    print(phonebook)
