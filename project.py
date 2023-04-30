import projClass
import re
import json
import datetime
from rich import print
from rich.console import Console
console = Console()

usersList = []
projectsList = []
def emailValidate():
    mailRegex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email = input("Enter Your Email: ")
    while(not re.match(mailRegex, email) ):
        email = input("Enter Your Email Correctly: ")
    return email
# def saveFile(obj, path):
#     loadFile(path)
#     usersList.append(obj)
#     file = open(path, "w")
#     json.dump(usersList, file, cls=projClass.UserEncoder)
#     #file.write(str(obj) + '\n') # == file.write(repr(obj) + '\n')
#     file.close()
# def loadFile(path):
#     file = open(path, "r")
#     lines = json.load(file)
#     for line in lines:
#         usersList.append(line)
#     file.close()   
def saveFile(obj, path):
    with open(path, 'a') as f:
        json.dump(obj, f, cls=projClass.UserEncoder)
        f.write("\n")
def saveProj(obj, path):
    with open(path, 'a') as f:
        json.dump(obj, f, cls=projClass.ProjEncoder)
        f.write("\n")

def loadFile(path):
    with open(path, 'r') as f:
     for line in f:
        obj = json.loads(line)
        usersList.append(obj)
def loadProj(path):
    with open(path, 'r') as f:
     for line in f:
        obj = json.loads(line)
        #print(line) #json
        #print(obj) #str
        projectsList.append(obj)

    
    

console.print("----------------------------------\n** WELCOME IN THE CROWD FUNDING ** \n----------------------------------\n", style="color(5)")
def register():
    
    console.print("REGISTRATION -> \n", style="color(5)")

    fName = input("\nEnter Your First Name: ")
    while (not fName.isalpha()):
        fName = input("Enter Your First Name Correctly: ")

    lName = input("Enter Your Last Name: ")
    while(not lName.isalpha()):
        lName = input("Enter Your Last Name Correctly: ")

    email = emailValidate()
        
    password = input("Enter Your Password ' > 6': ")
    while(len(password)<6):
        password = input("Enter Your Password Correctly: ")

    passwordConfirm = input("Repeat Your Password Again: ")
    while(passwordConfirm != password):
        passwordConfirm = input("Repeat Your Password Correctly: ")

    phoneNumber = input("Enter Your Phone Number: ")
    phoneRegex = "^01[0125][0-9]{8}$"
    while(not re.match(phoneRegex, phoneNumber) ):
        phoneNumber = input("Enter Your Phone Number Correctly: ")
    logged=False
    user = projClass.User(fName, lName, email, password, phoneNumber,logged)
    #usersList.append(user)
    print(user.__dict__)
    saveFile(user, 'users.json')

loginUser = {}
registeredUser = {}
def login():
    global loginUser
    console.print("\nLOGIN -> \n", style="color(5)")
    login=False
    while login==False:
        email = emailValidate()
        loadFile('users.json')
        #print(usersList)
        for user in usersList:
           # print(f"--\n{user}\n")
            if (user["email"] == email):
                loginUser = user 
                print(loginUser)                                                
                break                
        if(not loginUser):
            console.print("No User With This Credentials", style='red blink bold reverse frame')
        else:
         while(loginUser):
            password = input("Enter Your Password: ")
            if(loginUser["password"] == password):
                console.print(" You Are Logged In Mr {fName} ".format(**loginUser), style='green blink bold on white')
                loginUser["logged"] = True
                login = True
                print(loginUser)
                break
            else:
             console.print("Wrong Password For This User, Try Again", style='red blink reverse bold frame')
# register()
login()

def createProject():
   #who = input("Who Are You ? Enter Your Email Please: ")
   if "logged" in loginUser and loginUser["logged"] == True:
    loginEmail = loginUser["email"]
    console.print("PROJECT CREATION -> \n", style="color(5)")
    title = input("\nEnter Project Title: ")
    while (not title.isalpha()):
        title = input("Enter Project Title Correctly: ")

    details = input("Enter Project Details: ")
    while(not isinstance(details, str)):
        details = input("Enter Your Project Details Correctly: ")

    totalTarget = input("Enter Project Total Target: ")
    while(not totalTarget.isdigit()):
        totalTarget = input("Enter Your Project Total Target Correctly: ")
        
    reachedTarget = input("Enter Project Reached Target: ")
    while(not reachedTarget.isdigit() or reachedTarget > totalTarget):
        reachedTarget = input("Enter Your Project Reached Target Correctly: ")

    while True:
        try:
            startDate = input("Enter Project Start Date: (DD-MM-YYYY) ")
            datetime.datetime.strptime(startDate, "%d-%m-%Y")
            break
        except ValueError:
            print("Wrong Date Format. Please Try Again.")

    while True:
        try:
            endDate = input("Enter Project End Date: (DD-MM-YYYY) ")
            datetime.datetime.strptime(endDate, "%d-%m-%Y")
            break
        except ValueError:
            print("Wrong Date Format. Please Try Again.")
   
    proj = projClass.Projec(title, details, totalTarget, reachedTarget, startDate, endDate, loginEmail)
    print(proj.__dict__)
    saveProj(proj, 'projects.json')
   else:
       print("Sorry, You Are Not Logged In To Create -_-")

def editProject():
    wantedProject = {}   
    if "logged" in loginUser and loginUser["logged"] == True:
       loginEmail = loginUser["email"]
       yourProjectTitle = input("Enter The Title Of Your Project You Want To Modify Please: ")
       loadProj('projects.json')
       for proj in projectsList:
         if( proj["ownerEmail"] == loginEmail and  proj["title"] == yourProjectTitle):
            wantedProject = proj
            break
       if(wantedProject):
         print(wantedProject)
       else:
           print("You Have No Project With This Title")
           return

    else:
        print("Sorry, You Are Not Logged In To Edit -_-")
        return
    print(wantedProject)
    decision = input("Do You Want To Modify The Project Title ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
            title = input("\nEnter Project Title: ")
            while (not title.isalpha()):
               title = input("Enter Project Title Correctly: ")
            wantedProject["title"] = title
    decision = input("Do You Want To Modify The Project Details ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
         details = input("Enter Project Details: ")
         while(not isinstance(details, str)):
             details = input("Enter Your Project Details Correctly: ")
         wantedProject["details"] = details
    decision = input("Do You Want To Modify The Project Total Target ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
        totalTarget = input("Enter Project Total Target: ")
        while(not totalTarget.isdigit()):
            totalTarget = input("Enter Your Project Total Target Correctly: ")
            wantedProject["totalTarget"] = totalTarget
    decision = input("Do You Want To Modify The Project Reached Target ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
        reachedTarget = input("Enter Project Reached Target: ")
        while(not reachedTarget.isdigit()):
           reachedTarget = input("Enter Your Project Reached Target Correctly: ")
        wantedProject["reachedTarget"] = reachedTarget
    decision = input("Do You Want To Modify The Project Start Date ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
        while True:
          try:
            startDate = input("Enter Project Start Date: (DD-MM-YYYY) ")
            datetime.datetime.strptime(startDate, "%d-%m-%Y")
            break
          except ValueError:
            print("Wrong Date Format. Please Try Again.")
        wantedProject["startDate"] = startDate
    decision = input("Do You Want To Modify The Project End Date ? ")
    if(decision.lower() == "yes" or decision.lower() == 'y'):
        while True:
         try:
            endDate = input("Enter Project End Date: (DD-MM-YYYY) ")
            datetime.datetime.strptime(endDate, "%d-%m-%Y")
            break
         except ValueError:
            print("Wrong Date Format. Please Try Again.")
        wantedProject["endDate"] = endDate
    # else:
    #     pass
#    editProj = projClass.Projec(title, details, totalTarget, reachedTarget, startDate, endDate, loginEmail)
    print(wantedProject)
    saveProj(wantedProject, 'projects.json')

def showProjects():
    loadProj('projects.json')
    for proj in projectsList:
        print(proj)

def showProjWithDate():
    wantedProject = []   
    yourProjectDate = input("Enter The Date Of Your Project That You Want To Show Please: ")
    loadProj('projects.json')
    for proj in projectsList:
        if( proj["startDate"] == yourProjectDate or  proj["endDate"] == yourProjectDate):
            wantedProject.append(proj)
            
    if(wantedProject):
         print(wantedProject)
    else:
           print("You Have No Project With This Date")
           return
def fundProject():
    wantedProject = {} 
    if "logged" in loginUser and loginUser["logged"] == True:
        console.print("PROJECT DONATION -> \n", style="color(5)")
        projFundTitle = input("Enter Title Of Project You Want To Fund: ")
        loadProj('projects.json')
        for proj in projectsList:
             if( proj["title"] == projFundTitle):
                 wantedProject = proj
                 break
        if(not wantedProject):
           print("You Have No Project With This Title")
           return
        else:
           print(wantedProject)
           projFundMoney = int(input("Enter Amount Of Money You Want To Fund: "))
           wantedProject["reachedTarget"] = int(wantedProject["reachedTarget"]) + projFundMoney
        print(wantedProject)
        if(int(wantedProject["reachedTarget"]) == int(wantedProject["totalTarget"])):
            console.print("Thank You, We have reached Our Goal Thanks To You", style='green blink bold on white')
        saveProj(wantedProject, 'projects.json')
    else:
        print("You Can’t Donate Unless You Are Registered User")      


createProject()
#editProject()
#showProjects()
#showProjWithDate()
#fundProject()