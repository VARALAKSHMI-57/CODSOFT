contacts = []
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input(" Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added  successfully!\n")
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No Contacta found.\n")
        return
    for index,contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No Contacts found.\n")
        return
    for index,contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()
def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter Name or Phone NUmber: ").lower()
    Found = False
    for contact in contacts:
        if(search in contact['name'].lower()or
               search in contact['phone']):
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True
    if not found:
        print("Contact not found.\n")
def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter Phone Number of contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Leave blank if you dont want to change.")
            new_name    = input("Enter New Name: ")
            new_phone   = input("Enter New Phone: ")
            new_email   = input("Enter New Email: ")
            new_address = input("Enter New Address: ")
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact upload successfully!\n")
    print("Contact not found.\n")
def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter Phone Number of contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")
while True:
    print("======CONTACT BOOK ======")
    print("1. Add contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")        
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you for using Contact Book!")
        break 
    else:
        print("INvalid choice! Please try again.\n")          