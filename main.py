# task 1
import mood_responses
# mood = input("How are you feeling today? ")
# print(mood_responses.mood_response(mood))


# task 2.1
import contacts_manager

contact_dict = {}
contacts_manager.menu()
user_input = contacts_manager.valid_input()

while (user_input != 8): #loops until user wants to quit
    if (user_input == 1):
        
        name = input("Enter the name of the contact you wish to add: ")
        exist = contacts_manager.check_key(contact_dict, name)
        
        if exist:
            print("This contact already exist")
        else:
            type = input("What type of contact are you adding (Phone number, Email, Additional info)? ")
            
            label = contacts_manager.check_label(type)
            if label:    
                info = input("Enter in their contact: ")
                if type == "Email":
                    email = contacts_manager.check_email(info)
                    if email != []:
                        contacts_manager.add_contact(contact_dict, name, type, email)
                    else:
                        print("Incorrect email format")
                else:
                    contacts_manager.add_contact(contact_dict, name, type, info)
            else:
                print("Please choose only the following contact type (same spelling): Phone number, Email, Additional info")
                
    elif (user_input == 2):
        name = input("Enter the name of the contact you wish to edit: ")
        
        exist = contacts_manager.check_key(contact_dict, name)
        
        if exist:
            type = input("What type of contact are you editing (Phone number, Email, Addition info)? ")
            
            label = contacts_manager.check_label(type)
            if label:    
                info = input("Enter in their contact: ")
                if type == "Email":
                    email = contacts_manager.check_email(info)
                    if email != []:    
                        contacts_manager.edit_contact(contact_dict, name, type, email)
                    else:
                        print("Incorrect email format")
                else:
                    contacts_manager.edit_contact(contact_dict, name, type, info)
            else:
                print("Please choose only the following contact type (same spelling): Phone number, Email, Additional info")
                
        else:
            print("This contact does not exist")
    
    elif (user_input == 3):
        name = input("Enter the name of the contact you wish to delete: ")
        
        exist = contacts_manager.check_key(contact_dict, name)
        
        if exist:
            contacts_manager.delete_contact(contact_dict, name)
        else:
            print("This contact does not exist")
        
    
    elif (user_input == 4):
        name = input("Enter the name of the contact you wish to find: ")
        contacts_manager.search(contact_dict, name)
    
    elif (user_input == 5):
        
        contacts_manager.display_all(contact_dict)
        
    elif (user_input == 6):
        filename = input("What filename do you want to export your contacts to: ")
        contacts_manager.export(contact_dict, filename)
        
    elif (user_input == 7):
        filename = input("What filename do you want to import your contacts from: ")
        contacts_manager.import_contact(contact_dict, filename)
        
    # contacts_manager.menu()
    # user_input = contacts_manager.valid_input()   

from datetime import datetime

def display_curr_month_year():
    curr_date = datetime.now()
    month = curr_date.strftime("%B")
    year = curr_date.year
    
    print("current month:", month)
    print("current year:", year)

def parse_date(date_string):
    try:
        
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        print("Parsed date:", parsed_date)
    except ValueError:
        print("Invalid format -> YYYY-MM-DD")
        
        
display_curr_month_year()
    
user_input = input("Enter date (YYYY-MM-DD): ")

parse_date(user_input)


# task 3
import text_utils
reverse = input("Enter a string to reverse: ")

print(text_utils.reverse_string(reverse))

cap = input("Enter a string to capitalize: ")
print(text_utils.capitalize_string(cap))