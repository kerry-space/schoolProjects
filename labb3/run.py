from files import file_manager




class run:

    print("welcome to this program")
    choice = 0
    #sakapr en instans manag_files av klassen file_manager
    manag_files = file_manager()
    searched_list = []  
    
    
    
    
    while choice !=4:
        print("------------------------------------------------------------------------")
        print("choice between one of the meny options\n1:Search for the movies\n2:show the last searched movies \n3:End the programmet\n")
        print("-------------------------------------------------------------------------")

        try: 
           choice = int(input("choose: "))
            
        except ValueError:
            print("skriv in rätt meny val ")
            continue     

        if choice == 1:
            searching_field = input("search your movie: ")
            searched_list.append(searching_field)
           #replace tomma mellan slag med + ex walk+of+fame
            serach_URL = searching_field.replace(" ", "+")
            print("-------------------")
            if len(searched_list) > 5:
                searched_list.pop(0)
            manag_files.search_def(serach_URL)
        
        elif choice == 2:
            if len(searched_list) > 0:
                manag_files.last_serached(searched_list)
            else:
                print("no searching History is founded")
                
            
        elif choice == 3:
            print("------------------------------------------------------------")
            print("The program is ended,Bye and see you again next time")
            print("------------------------------------------------------------")
            break
    
        else:
            print("Please choose one of the option in the meny")





 
  