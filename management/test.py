"""
Usage: test.py --p=N 

Arguments:
    TEXT  Message to be printed

Options:
    --p=N  number of times users will be generated
    --caps  convert the text to upper case
"""

from management import User
from management import Account
from user_dict import names
from docopt import docopt
import random


from mongoengine import *

# https://code.google.com/p/prettytable/
#  https://code.google.com/p/prettytable/source/browse/trunk/README

connect ('user')#, port=27777)
    
first_name = "abc"
last_name = "abc"
    
def generate_firstname():
    num1 = random.randint(0,4)
    return names[num1]

def generate_lastname():
    num2 = random.randint(0,4) 
    return names[num2]
    
def get_names():
    first_name = generate_firstname()
    last_name = generate_lastname()
    

def generate_user():
    get_names()
    user = User(title="Mr.", 
                firstname = first_name,
                lastname= last_name,
                email= first_name+ last_name+"@gmail.com").save()
                     
    account = Account(username= first_name + last_name,
                      email= first_name + last_name+"@gmail.com",
                      password="17ROW1992")
    account.owner = user
    account.id
    account.save()
    print first_name + last_name

def print_summary(): 
    #generate_user()     
    print "\nLIST OBJECTS"
    print 70 * "-"
    print

    accounts = Account.objects()

    for account in accounts:
        print account.owner.firstname, ":", account
        print account.id

    print "\n" + 70 * "-"
    
    delete_user()

def print_contacts(columns):
    pass 

def delete_user():
    accounts = Account.objects()
    #del accounts
    #accounts = None
    for account in Account.objects:
        print "deleted***************************"
        account.delete()
        print "deleted***************************"
    
    #for account in accounts:
        #print account.owner.firstname, ":", account
        

print_contacts(["username", "phone", "email"])

#print_summary()

if __name__ == '__main__':
    print "This is an example use of docopt"
    
    try:
        arguments = docopt(__doc__)
        
        p = int(arguments['--p'])
        
        for i in range(p):
            print_summary()
            
    except DocoptExit as e:
        print e.message


"""how many users from bloomington
   how many from chicago
   mhao many for that isntitue"""

   
   
