from datetime import datetime
import os

contacts = []

def load_contacts(contacts):
    if os.path.exists("contacts.txt"):
        with open("contacts.txt","r") as f:
            for row in f:
                row = row.strip()
                if row:
                    parts = row.split(",")
                    contacts.append({
                        "name": parts[0],
                        "number": parts[1],
                        "date": parts[2]
                        })
                
def add_contact(contact):
    try: 
        now = datetime.now()
        date = now.strftime(" %d/%m/%Y ")
        name = input("Add a name for a new contact: ")
        number = int(input("Add a phone number for the new contact: "))
        contact.append({"name": name, "number": number , "date": date})
        print("contact added!")
    except ValueError:
        print("error")

def view_contacts(contacts):
    if len(contacts) == 0 :
        print("No contacts yet!")
    else :
        for Contact in contacts:
            print(f"name : {Contact['name']} | number : {Contact['number']} | date : {Contact['date']}")
            
def search_contact(contacts):
    try:
        name = input("inter a name you want to search for : ")
        found = False
        for Contact in contacts: 
            if name == Contact["name"]:
                print(f"name : {Contact['name']} | number : {Contact['number']}")
                found = True
        if found == False:
            print("Contact not found!")
    except ValueError:
        print("you have not put a name")

def save_contacts(contacts):
    with open("contacts.txt","w") as f:
        for Contact in contacts:
            f.write(f"\n{Contact['name']},{Contact['number']},{Contact['date']}")

load_contacts(contacts)

while True:
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Quit")
    try: 
        answer = int(input("choose an option: "))
        if answer == 1:
            add_contact(contacts)
        elif answer == 2:
            view_contacts(contacts)
        elif answer == 3:
            search_contact(contacts)
        elif answer == 4:
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("invalid option")
    except ValueError :
        print("you have not chose a number")