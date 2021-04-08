import random 
database = {} 

def init(): 
    
    print('Welcome to Bank Python') 

    haveaccount = int(input('Do you have an account with us? 1(Yes) 2 (No) \n')) 
    
    if(haveaccount == 1):
        
        login() 
    elif(haveaccount == 2): 

        register() 
    else: 
        print('You have selected an invalid option') 
        init() 

def login(): 
    print('===== LOGIN =====')

    accountnumberfromuser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountnumber,userdetails in database.items(): 
        if(accountnumber == accountnumberfromuser):
            if(userdetails[3] == password):
                bankoperation(userdetails) 

    print('Invalid account or password, you have one more try')
    login2() 

def login2(): 
    print('===== LOGIN AGAIN =====')

    accountnumberfromuser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountnumber,userdetails in database.items():  
        if(accountnumber == accountnumberfromuser):
            if(userdetails[3] == password):
                bankoperation(userdetails) 

    print('Too many incorrect entries')
    init() 
   

def register(): 
    print('=====Register======')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password \n')
   

    accountnumber = generateanaccountnumber() 

    database[accountnumber] = [first_name, last_name, email, password] 
    
    print('Your account has been created!')
    print('==== ==== ====== ====')
    print('Your account number is: %d' % accountnumber)
    print('Make sure you keep it safe!')
    print('==== ==== ====== ====')

    login() 

def bankoperation(user):

    print('Welcome %s %s!' % ( user[0], user [1] ) )

    selectedoption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))
    
    if(selectedoption == 1):
       
        depositoperation()
    elif(selectedoption == 2):
        
        withdrawaloperation() 
    elif(selectedoption == 3):
        
        logout() 
    elif(selectedoption == 4):
        
        exit()
    else:
        
        print('Invalid option selected')
        bankoperation(user)

def withdrawaloperation():
    print('Withdrawal')
    withdraw=input('How much would you like to withdraw? \n')
    print('Take your cash')
    bankoperation2()

def depositoperation():
    print('Deposit')
    deposit=input('How much would you like to deposit? \n') 
    print('You selected to deposit %s' % deposit)
    bankoperation2()


def bankoperation2():

    selectedoption = int(input('Would you like to perform another function? (1) Yes (2) No \n'))

    if(selectedoption == 1):
        bankoperation3()

    elif(selectedoption == 2):
        exit() 
    
    else:
        
        print('Invalid option selected')
        logout()

def bankoperation3():
    
    selectedoption2 = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))
    
    if(selectedoption == 1):
       
        depositoperation()
    elif(selectedoption == 2):
        
        withdrawaloperation() 
    elif(selectedoption == 3):
        
        logout() 
    elif(selectedoption == 4):
        
        exit()
    else:
        
        print('Invalid option selected')
        bankoperation()


def generateanaccountnumber(): 
    return random.randrange(1111111111,9999999999) 

def logout():
    login() 
    
init() 

