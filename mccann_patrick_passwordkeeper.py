website = []#creates an empty list
username = []
password = []

def get_password(): #defines function
    web = input("website name")#asks user for the website name
    user = input("username")
    pass_ = input("password")
    website.append(web)# adds input to empty list
    username.append(user)
    password.append(pass_)

def get_entries():
    for i in range(len(website)):# for the amount of items in the list
            print (website[i], username[i],password[i])#prints the items in list
            
def get_info():
    while True:#forever
            info = input("what website are you looking for")#user input
            if info in website:# if the input is in the lsit
                index = website.index(info)# gets the item's index
                print (username[index],password[index])# prints the corresponding info
                break#ends forever loop
            else:#everything else
                print("this website does not have an entry")#invalid message
                
def change_entry():
    while True:
        question = input("what website's info are you changing?")
        if question in website:
            stuff = website.index(question)
            while True:
                question_2 = input("what info are you changing?")
                if question_2 == "website":
                    question_3 = input("what are you changing the info to?")
                    website[stuff] = question_3#changes info
                    break
                elif question_2 == "username":
                    question_3 = input("what are you changing the info to?")
                    username[stuff] = question_3
                    break
                elif question_2 == "password":
                    question_3 = input("what are you changing the info to?")
                    password[stuff] = question_3
                    break
            
                else:
                    print("Only one piece of info at a time")
                    
            break
        else:
            print("this website does not have an entry")
            
        
def check_password():
    webname = input("what website's passowrd are you checking")
    if webname in website:
        passkey = website.index(webname)
        counter = 0#adds counter
        key = list(password[passkey])#makes the item into a list
        for i in range(len(key)):
            if i in ["!","@","#","$","%","^","&","*","1","2","3","4","5","6","7","8","9","0"]:#if the element contains these items
                counter += 1#raises counter by one
                if counter > 3:#if the counter is larger than 3
                    print("you have a good password")
                else:
                    print("this is a bad passowrd")
            else:
                print("this is a bad passowrd")
 
    else:
        print("this website does not have an entry")
def delete_entry():
    while True:
        i = input("what website are you deleting?")
        if i in website:
            dex = website.index(i)
            del website[dex]#deletes item
            del username [dex]#deletes item
            del password [dex]#deltes item
            break
        else:
            print("this website does not have an entry")
        


while True:
    menu = input("""
options:
a to add an entry
b to see all entries
c to access specific info
d to change an entry
e to check passowrd security
f to delete an entry
q to quit
""").lower()#makes all answers lowercase

    if menu == "a":
        get_password()
    elif menu == "b":
        get_entries()
    elif menu == "c":
        get_info()
    elif menu == "d":
        change_entry()
    elif menu == "e":
        check_password()
    elif menu == "f":
        delete_entry()
    elif menu == "q":
        break
    else:
        print("only an option in the option list")
