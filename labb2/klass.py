import csv
import json



def read_orginal_fil(filename, json_file):

    
    new_lines = []

    name_info = ("username", "Fname", "Enamn", "email" )

    try:
        with open(filename, "r", encoding="utf-8-sig") as csv_file:
            save_data = csv.DictReader(csv_file, name_info, delimiter = ";")#comma separated values(csv) delimiter anger typ av citat kräkter separe olika elar i filen ex , ;
            for entry in save_data:
                for category in entry:
                    entry[category] = entry[category].strip()
                new_lines.append(entry)
            new_lines.pop(0)
        
        
       
    except FileNotFoundError as ferr:
        print(ferr)

    #create json file
    try:
        with open(json_file, "w", encoding="utf-8-sig") as file_obj:
            json.dump(new_lines, file_obj)

    except FileNotFoundError as ferr:
        print(ferr)
    
    return new_lines
   


def show_list(new_lines):

    #print out the lsit
    if len(new_lines) > 0:
        for person in new_lines:
            print(person)
    else:
        print("The content of list is empty")


def show_json_data(json_list):
    try:
        with open(json_list, "r", encoding="utf-8-sig") as json_obj:
            content = json.load(json_obj)
        for row in content:
            print(row)
    except FileNotFoundError as ferr:
        print(ferr)
   


def add_person(persons_list):
    username = ""
    fname = ""
    enamn = ""
   

    while not username:
        username = input("username: ").strip()

    while not fname:
        fname = input("fname: ").strip()
    while not enamn:
        enamn = input("enamn: ").strip()
    
    
    new_person = {"username": username, "fname": fname, "enamn": enamn,"email": username + '@du.se'}
    persons_list.append(new_person)
    print("The person is addad to the list")
    return persons_list



def remove_person(persons_list):
    
    r_user_name = input("Enter the username of person you want to remove from list: ")
    for person in range(len(persons_list)):
        if persons_list[person]["username"] == r_user_name:
            del persons_list[person]
            print(f"\n{remove_person} is removed from the list")
            break

    return persons_list
    



def save_fil(json_file, persons_list):

    try:
        with open(json_file, "w", encoding="utf-8-sig") as file_obj:
            json.dump(persons_list, file_obj)#våran person_list ska skrivas till filen file_obj allstå json_file som öppnades 
            
    except FileNotFoundError as ferr:
       print(ferr)
    print("\nYour list is saved to save.json file")
    
