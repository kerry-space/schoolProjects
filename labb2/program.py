from klass import read_orginal_fil, show_list ,show_json_data, add_person, remove_person, save_fil
cvs_file = "labb2-personer.csv"
json_file = "save.json"
persons_list = []


def startup():
    print("welcome to this program")
    choice = 0

    while choice !=7:
        print("------------------------------------------------------------------------")
        print("choice between one of the meny options\n1:Read the orignal file (personer.csv)\n2:Show the list\n3:Show json-data\n4:Add a person\n5:Remove a person\n6:Save to fil\n7:End the programmet\n")
        print("-------------------------------------------------------------------------")

        try: 
           choice = int(input("choose: "))
            
        except ValueError:
            print("skriv in rätt meny val")
            continue     

        if choice == 1:
            persons_list = read_orginal_fil(cvs_file, json_file)
        
        elif choice == 2:
            show_list(persons_list)
        elif choice == 3:
            show_json_data(json_file)       
        elif choice == 4:
            persons_list = add_person(persons_list)
            
        elif choice == 5:
            persons_list = remove_person(persons_list)
        elif choice == 6:
            save_fil(json_file, persons_list)
        elif choice == 7:
            print("------------------------------------------------------------")
            print("The program is ended,Bye and see you again next time")
            print("------------------------------------------------------------")
            break
        else:
            print("Please choose one of the option in the meny")




startup()