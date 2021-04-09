#register
#login
import random
database = {}
accountBalance = {}

#definining initialization function
def init():
    ValidOptionSelected = False
    print('Welcome to Bank LDA')
    while ValidOptionSelected == False:
        
        haveAccount = int(input ('Do you have an accont with us? Please select (1) for Yes and (2) for No \n'))
        
        if (haveAccount == 1):
            ValidOptionSelected = True
            login()

        elif(haveAccount == 2):
            ValidOptionSelected = True
            register()
        else:
            print("You have selected an invalid option")
            init()
    

def login():
    print('****Login******')
    acctNumberFromUser = int(input('What is your Account Number?\n'))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
        if (accountNumber == acctNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)
    
    else:
        print('Invalid account or password')
        login()


def register():
        print('****** Kindly Register *****')
        email = input('What is your email address? \n')
        first_name = input('What is your First Name? \n')
        last_name = input('What is your Last Name? \n')
        password = input('Create a password \n')
        accountNumber = generateAccountNumber()
        database[accountNumber] = [first_name, last_name, email, password]
        print('Your account has been created')
        print('******************')
        print('Your account number is: %s' %accountNumber)
        print('Please keep your account number confidential')
        print('******************')

        login()

        


def bankOperation(user):
    print('Welcome %s %s' %(user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        Exit()
    else:
        print('Invalid Option Selected')
        bankOperation(user)


def depositOperation():
    deposit= int(input('How much would you like to deposit \n'))
    print('***********')
    print('Deposit Successful')
    

def withdrawalOperation():
    print('This is withdrawal operation')

def logout():
    print('This is logout operation')

def Exit():
    print('This is Exit operation')




def generateAccountNumber():
    return  random.randrange(111111111,999999999)

###  ACTUAL BANKING SYSTEM ###


init()
