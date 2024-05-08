import os

run = True

while run:
    direc = "C:\\Users\\aydip\\contacts for one of my projects"
    os.chdir(direc)
    to_do = input("What would you like to do? (add contacts/delete contacts/view contact/check contacts list/rename/leave) ").lower().strip()
    if to_do.startswith("a"):
        # Namming and creating files
        contact_name = input("Contact name: ")
        folder = open(f'{contact_name}.txt', 'w')
        
        # Variables
        fullname = input("Full name: ")
        phone = input("Phone number: ")
        home_address = input("Home address: ")
        email_address = input("Email address: ")
        additi_inf = input("Additional information: ")
        
        # Checking if variables DON'T meet the conditions
        
        if fullname == '':
            print("This is necessary information. Try again. ")
            fullname = input("Full name: ")
            
            if len(fullname) < 2:
                print(f"\"{fullname}\" is an invalid argument, it's too short. The program is ending... ")
                run = False
        
        elif len(fullname) < 2:
            print(f"\"{fullname}\" is an invalid argument, it's too short. The program is ending... ")
            run = False

        if phone == '':
            phone = "skipped"

        elif len(phone) < 10:
            print(f"\"{phone}\" is an invalid argument, it's too short. The program is ending... ")
            run = False

        if home_address == '':
            home_address = "skipped"

        elif len(home_address) < 5:
            print(f"\"{home_address}\" is an invalid argument, it's too short. The program is ending... ")
            run = False
        
        if email_address == '':
            email_address = "skipped"
        
        elif len(email_address) < 11:
            print(f"\"{email_address}\" is an invalid argument, it's too short. The program is ending... ")
            run = False
        
        if additi_inf == '':
            additi_inf = "skipped"

        # Writing on the file
        folder.write(f"Full name: {fullname}\n")
        folder.write(f"Phone number: {phone}\n")
        folder.write(f"Home address: {home_address}\n")
        folder.write(f"Email address: {email_address}\n")
        folder.write(f"Additional information: {additi_inf}\n")
        
        # Saving the data
        save = input("Press enter to save ")
        if save == "":
            folder.close()
        else: 
            folder.close()
            print("File did not save")
            os.remove(f"{direc}\\{contact_name}.txt")
    
    # Searching for a contact
    elif to_do.startswith("v"):
        search_name = input("Search for ").strip("\"").strip()
        try: 
            os.startfile(f"{direc}\\{search_name}.txt")
        except:
            print("Contact not found")
    
    # Delete a contact
    elif to_do.startswith("d"):
        contact_name = input("Contact to delete: ").strip("\"").strip()
        try: 
            os.remove(f"{direc}\\{contact_name}.txt")
        except:
            print("Contact not found")

    elif to_do.startswith("l"):
        run = False

    # Check the name of concacts
    if to_do.startswith("c"):
        list_of_contacts = os.listdir(direc)
        print("Your contacts are:", end=' ')
        if list_of_contacts == []:
            print("Empty, no contacts")
        
        else:        
            print(list_of_contacts)
    
    # Rename a contact
    if to_do.startswith("r"):
        os.startfile(direc)