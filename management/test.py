"""
Usage: 
    test.py --del=N
    test.py --gen=N
    test.py --find=N

Arguments:
    TEXT  Message to be printed

Options:
    --del=N  	number of users to be deleted
    --gen=N 	number of users to be created
    find	prints all users
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
    
x = 0

first_name = "abc"
last_name = "abc"
    
def generate_firstname():
    num1 = random.randint(0,4)
    return names[num1]

def generate_lastname():
    num2 = random.randint(0,4)
    return names[num2]
    

def generate_user():
    for i in range(p):
    	first_name = generate_firstname()
    	last_name = generate_lastname()
    	print
    	print last_name
    	print "I am here"
    	print 
    	print
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
    
    print_summary()

def print_summary():      
    print "\nLIST OBJECTS"
    print 70 * "-"
    print

    accounts = Account.objects()

    for account in accounts:
        print account.owner.firstname, ":", account
        print account.id

    print "\n" + 70 * "-"
    

def print_contacts(columns):
    pass 

def delete_user():
    accounts = Account.objects()
    i = 0
    print i,p
    #del accounts
    #accounts = None
    for account in Account.objects:
    	i = i + 1
        if i < p:
        	account.delete()
    
    for account in accounts:
        print account.owner.firstname, ":", account
        
def find_user(name):
    accounts = Account.objects()
    
    for account in Account.objects:
    	if account.owner.firstname == name:
    		print account.owner.firstname, ":", account
        

print_contacts(["username", "phone", "email"])

#print_summary()

if __name__ == '__main__':
    print "This is an example use of docopt"
    
    #try:
    arguments = docopt(__doc__)
        
    if (arguments["--del"]):    
    	p = int(arguments['--del'])
        delete_user()
    elif(arguments["--gen"]):    
    	p = int(arguments['--gen'])
        generate_user()
    elif(arguments["--find"]):
    	user = arguments['--find']
    	find_user(user)
            
    #except DocoptExit as e:
     #   print e.message


"""how many users from bloomington
   how many from chicago
   mhao many for that isntitue"""

   
   
