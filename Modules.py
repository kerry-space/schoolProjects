

#skapa minst två funktioner 

#funktion 1. tar emot två tal i sin parameterlista, Utifrån dessa två tal ska det returneras en lista med de tal från 1 till 1000 som är delbara till heltal.
def delbar_hetal(tal1, tal2):
    
    # tom lista 
    number_list = []
    #loopar från 1-100 kollar om i talet är delbar tal1 och tal2, returnera sen listan
    for i in range(1, 101):
        if i % int(tal1) == 0 and i % int(tal2) == 0 and i:
            number_list.append(i)
    return number_list





# funktion 2. låta användaren gissa på ett tal mellan 1 och 100.
def gissa_tal():

    print("välkomma till gissningstal")
    
    #includerar rand funktioen
    from random import randint
    gissa_slump = randint(1, 101)
   
   # loopen körs så länge du gissar rätt tal
    while True:
        # kollar så att användaren skriver in bara interiger, siffra
        while True:
            try:
                gissa = int(input("gissa ett tal mellan 1-100: "))
                break
            except ValueError:
                print("skriv bara number..")
        
        if gissa == gissa_slump:
            print("grattis du gissade rätt")
            break
        elif gissa > gissa_slump:
            print("talet var större")
        elif gissa < gissa_slump:
            print("talet är mindre")
            
        
        