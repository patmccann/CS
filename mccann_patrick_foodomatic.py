#Code written by Patrick McCann
#Code genereates a random accusation for the board game Clue
#4/6/2025
#New Domain, Detects inputs that are not numbers and displays error message
#Samantha Marciano, Python_How_To

import random  #allows code to use randomizers

person = ["Miss Scarlet", "Mrs. Peacock", "Mr. Green", "Professor Plum", "Colonel Mustard", "Mrs. White"] #creates a list
weapon = ["candlestick", "lead pipe", "wrench", "knife", "revolver", "rope"] #creates a list
room = ["Hall", "Lounge", "Dining Room", "Kitchen", "Ballroom", "Conservatory", "Billiard Room", "Library", "Study"] #creates a list

while True: #Forever
    again = input("want an accusation? ")#User input
    
    if again == "no": #detects user input as no
        break #ends Code
    elif again == "yes": #detects user input as yes
        while True: #another Forever
            try: #pauses code to run a small section of code for errors
                accusation = int(input("How many accusations do you want to make? (numbers only)")) #asks number of accusations requested     
            except ValueError: #excludes ValueError as an input
                print ("numbers only") #if Value Error detected print numbers only
                continue #Continues running the code regularly
            for i in range(accusation): #for the indext in one of the lists
                p = random.choice(person)#creates a random selection from the person list
                print("in the", random.choice(room), "with the",weapon[person.index(p)],p)
                #prints a random choice of the room list, uses paralell arrays to make a slecetion from
                #the weapon list in the same location as the person list
            break #ends the second forever loop
    else: #if the first input is not yes or no
        print("yes or no?")#Requests the user to reply yes or no
            
    
   
    
