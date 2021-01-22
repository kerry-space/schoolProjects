#importera specifika funktioner från modules
from Modules import delbar_hetal, gissa_tal

def startup():
    print("välkommen till programmet")
    val_menu = 0
    while val_menu != 3:
       
        print("------------------------------------------------------------------------")
        print("välja en utav valen i meny\n1:delbar talen\n2:gissa ett tal\n3:Avsluta programmet")
        print("-------------------------------------------------------------------------")

        try: 
            val_menu = int(input("tal:"))
            
        except ValueError:
            print("skriv in rätt meny val")
            continue
        if val_menu == 1:
            print_delbar_tal()
        elif val_menu == 2:
            gissa_tal()
        elif val_menu == 3:
            print("programmet avslutas")
            break
            

def print_delbar_tal():
   
    #frågar användaren efter tal spara num_1 - num_2
    
    while True:
        try:
            num_1 = int(input("skriv en tal mellan 1-100: "))
            num_2 = int(input("skriv en till tal mellan 1-100: "))
            break
        except ValueError:
            print("skriv ett nummer som är från 1-100")
            
   
    #anropar funcktione delbar_hetal och tar emot return värdet i num_list
    num_list = delbar_hetal(num_1,num_2)    
    
    #print ut våran tal lista num-list
    print("----------------------")

    if num_list != []:
        print(f"Talen som är delbara med {num_1} och {num_2}")
        for numb in num_list:
            print(numb) 
            
    else:
        print("dessa två talen var inte delbara")

   

#anropa funktionen för start meny
startup()


