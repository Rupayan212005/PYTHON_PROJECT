contact={}

def add_contact():
    name=input("Enter Name: ")
    phone=input("Enter Phone Number : ")
    email=input("Enter Email : ")
    address=input("Enter Address: ")
    
    contact[name]={"Phone":phone,"Email":email,"Address":address}
    print("CONTACT ADDED!\n")

def delete_contact():
    name=input("Enter name that you want to delete :")
    if name in contact:
        del contact[name]
        print("Contact deleted")
    else:
        print("Name not found")

def search_contact():
    name=input("Enter Name :")
    if name in contact:
        print(f"Name:{name}")
        print(f"Phone:{contact[name]['Phone']}")
        print(f"Email:{contact[name]['Email']}")
        print(f"Address:{contact[name]['Address']}")
    else:
        print("Name not found!\n")

def update_contact():
    name=input("Enter name that you want to update:")
    if name in contact:
        phone=input("Enter phone number :")
        email=input("Enter Email :")
        address=input("Enter address :")
        contact[name]={"Phone":phone,"Email":email,"Address":address}
        print("CONTACT UPDATED!")
    else:
        print("Name not found!\n")

def view_contact():
    if not contact:
        print("Contact book is empty")
    else:
        for name,info in contact.items():
            print(f"Name:{name}")
            print(f"Phone:{info['Phone']}")
            print(f"Email:{info['Email']}")
            print(f"Address:{info['Address']}")



def start():
    while True:
        print("####CONTACT BOOK####")
        print("1 FOR ADD CONTACT")
        print("2 FOR DELETE CONTACT")
        print("3 FOR SEARCH CONTACT")
        print("4 FOR UPDATE CONTACT")
        print("5 FOR VIEW CONTACT")
        print("6 FOR EXIT")


        choice=input("Enter a choice:")
        if choice=="1":
            add_contact()
        elif choice=="2":
            delete_contact()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice=="5":
            view_contact()
        elif choice=="6":
            print("####GOOD BYE####")
            break
        else:
            print("INVALID OPTION!")
start()
        