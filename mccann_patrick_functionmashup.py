#patrick mccann
#function mashup
#5/29/2025

import random #imports random library
listone = ["A","B","C","D","E","F"] #creates list




def chorus(): #defines function
    print (""" 
            Sweet home Alabama
            Where the skies are so blue
            Sweet home Alabama
            Lord, I'm comin' home to you""") #print statment
def sing():
    print ("""
                    Big wheels keep on turnin'
                    Carry me home to see my kin
                    Singin' songs about the Southland
                    I miss Alabamy once again, and I think it's a sin, I said
                    Well, I heard Mr. Young sing about her
                    Well, I heard old Neil put her down
                    Well, I hope Neil Young will remember
                    A Southern man don't need him around, anyhow""")
    chorus()#calls the chorus function
    print("""
                    In Birmingham, they love the governor (boo, boo, boo!)
                    Now we all did what we could do
                    Now Watergate does not bother me, uh-uh
                    Does your conscience bother you? Tell the truth
                    Sweet home Alabama
                    Where the skies are so blue
                    Sweet home Alabama
                    Lord, I'm comin' home to you 
                    Speak your mind
                    Ah-ah-ah, Alabama
                    Ah-ah-ah, Alabama
                    Ah-ah-ah, Alabama
                    Ah-ah-ah, Alabama
                    Now Muscle Shoals has got the Swampers
                    And they've been known to pick a song or two 
                    Lord, they get me off so much
                    They pick me up when I'm feelin' blue, now how 'bout you?""")
    chorus()
    chorus()


def add(a, b):#creates function with two parameters
    print(a+b)#adds the parameters

def print_list(listone):
    for item in listone:#takes an item from a list
        print(item)#prints item

def in_list(listone, element):
    return element in listone #returns an element from a list
    print (element in listone)#prints an element from the list
            
def is_integer (parameter):
    try: #tries a line of code
        int(parameter)#checks if the parameter is an integer
        return True #returns True if it is an integer
    except ValueError: #exepct if there is an error with the value
        return False #then it returns false
def get_integers():
    while True: #forever
        numbers = input("Enter two numbers").split(",")#asks user for an input and then splits input by the comma creating a list
        for i in range(1):#one time
            if not is_integer(i):#if the input is not an integer
                print("two numbers seperated by a comma")#prints error message
            else:#otherwise
                a =  int(numbers[0])#a = the first number inputed
                b = int(numbers[1])#b = the second inputed
                return (a,b)#returns the numbers
        break#breaks loop
def get_random():
    a,b = get_integers()#calls a previous function
    print (random.randint(a,b))#prints a rondom number between the two numbers from the previous function
            

def get_vowels(word):
    counter = 0#sets counter to 0
    wordlist = list(word.lower())# turns input into a list
    for i in wordlist:#for the number of items in the list
        if i in ["a","e","i","o","u"]:# chechks the number of vowels
            counter += 1#adds one to the counter

    print(f"you have {counter} vowels")#prints the final number of vowels
            
def get_initials(fullname):
    names = fullname.split(" ")#takes the input and makes lists split by a space
    initials = ''#creates and empty string
            
    for name in names:#for the number of items in the lsit of names
        initials += name[0]#counts the number of names and takes the first letter
        return initials#returns the intials

def main():#main funciton
    while True:#forever
        menu = input("""What function would you like to run? Type a for sing, b for add, c for print_list,
d for in_list, e for is_integer, f for get_integers, g for get_random, h for get_vowels, i for get_initials, or q to quit""").lower()#input with automatic lowercasing
        if menu == "a":#checks if input is this
            sing()#calls function based on user request
        elif menu == "b":
            add(1,2)            
        elif menu == "c": 
            print_list(listone)            
        elif menu == "d":
            in_list(listone,'a')            
        elif menu == "e":
            is_integer('numbers')           
        elif menu == "f":
            get_integers()            
        elif menu == "g":
            get_random()
        elif menu == "h":
            get_vowels(input("type in a word"))
        elif menu == "i":
            print(get_initials(input("Enter your full name: ")))
        elif menu == "q":
            break
        else:
            print("only one of the listed options")#if the user did not meet requirements then this message is displayed
              
main()#calls main function
        

