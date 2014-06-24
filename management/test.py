"""
Usage: 
    test.py gen  [rand]
    		 [--num=N]
    test.py del	 [all]
    		 [--num=N]
    		 [--user=name]    		 
    test.py find [all]
    		 [--user=name]
    		 [--city=user_city]

Arguments:
    TEXT  Message to be printed

Options:
    --del=N  	number of users to be deleted
    --gen=N 	number of users to be created
    find	prints all users
"""


# https://code.google.com/p/prettytable/
#  https://code.google.com/p/prettytable/source/browse/trunk/README

from management import User
from management import Account
from user_dict import names
from docopt import docopt
from mongoengine import *
import random


connect ('user', port=27777)


first_name = "abc"
last_name = "abc"

accounts = Account.objects()
    
def generate_firstname():
    num1 = random.randint(0,4)
    return names[num1]

def generate_lastname():
    num2 = random.randint(0,4)
    return names[num2]
    

def generate_user():
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
    
    for account in accounts:
        print account.owner.firstname, ":", account
        print account.id

    print "\n" + 70 * "-"
    

def print_contacts(columns):
    pass 

def delete_user():
    i = 0
    for account in Account.objects:
        if i < p:
        	account.delete()
        i = i + 1
    
    for account in accounts:
        print account.owner.firstname, ":", account

def delete_all():
    for account in Account.objects:
        	account.delete()
        	
def delete_account(name):
    for account in Account.objects:
    	if account.owner.firstname == name:
    		account.delete()
        
def find_user(name):
    print
    Account.objects(firstname = name).count()
    print count
    print
    print
    for account in Account.objects:
    	if account.owner.firstname == name:
    		print account.owner.firstname, ":", account
        

print_contacts(["username", "phone", "email"])

if __name__ == '__main__':
    #try:
    arguments = docopt(__doc__)
        
    if(arguments["gen"]):
    	if(arguments["rand"]):
    		p = 10
    		for i in range(p):
    			generate_user()
    	elif(arguments["--num"]):
    		p = int(arguments['--num'])
    		for i in range(p):
    			generate_user()
    elif (arguments["del"]):                                      
    	if(arguments["all"]): 
    		delete_all()
    	elif(arguments["--user"]):
    		user = arguments['--user']
    		delete_account(user)
    	elif(arguments["--num"]):
    		p = int(arguments['--num'])
    		delete_user()
    elif(arguments["find"]):
    	if(arguments["all"]):
    		print_summary()
    	elif(arguments["--user"]):
    		user = arguments['--user']
    		find_user(user)
            
    #except DocoptExit as e:
     #   print e.message


"""how many users from bloomington
   how many from chicago
   mhao many for that isntitue"""

   
   
