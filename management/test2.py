"""
Usage: 
    test2.py -h
    test2.py gen [rand]
    		 [--num=N]
    test2.py add [--file=N]
    		 [--line=N]
    test2.py del [all]
    		 [--num=N]
    		 [--user=name]    		 
    test2.py find[all]
    		 [--user=name]
    		 [--city=user_city]

Arguments:
    del		 deletes users
    gen		 generates users
    find	 finds and prints out user information

Options:
    -h	         : show this help message
    rand	 : for generating random users
    --all  	 : performs a particular function to all the users
    --add=ARG    : adds users to the database in this fashion= 
    		   "first name"/"last name"/"username"/"email".
    		   Note that the backslash "/" must seperate these
    		   arguments.
    --num=ARG 	 : performs an operation to a number of users
    --user=ARG   : performs an operation on specific users
    --city=ARG 	 : prints all users
"""

# https://code.google.com/p/prettytable/
# https://code.google.com/p/prettytable/source/browse/trunk/README

from user import User
from management import Account
from user_dict import *
from docopt import docopt
from mongoengine import *
import random
import yaml

connect ('user', port=27777)


"This class generates random users"

class generate_random_user():
    
    accounts = Account.objects()
    
    user_info = []
    first_name = "abc"
    last_name = "abc"
    phone = "abc"
    inst = "abc"
    city = "abc"
    country = "abc"
    p = 10
    
    def generate_random(self):
    	num = random.randint(0,3)
        self.phone = phone[num]
        self.inst = institution[num]
        self.city = city[num]
        self.country = country[num]
        print self.city + self.country + self.inst + self.phone
    
    def generate_firstname(self):
        num1 = random.randint(0,4)
        return names[num1]

    def generate_lastname(self):
        num2 = random.randint(0,4)
        return names[num2]
    
    def get_names(self):
        self.first_name = self.generate_firstname()
        self.last_name = self.generate_lastname()

    def add_user(self):
        user = User(title="Mr.",
        	firstname = self.user_info[0],
        	lastname= self.user_info[1],
        	email= self.user_info[3]
                     ).save()
                     
        account = Account(username=self.user_info[2],
                  email=self.user_info[3],
                  password="17ROW1992",
                  phone = self.phone,
                  department = "School of Informatics and Computing",
                  institution = self.inst,
                  adviser_contact = "Bloomington, Indiana",
                  institute_address = self.city,
                  institute_country = self.country,
                  url = "www.google.com",
                  citizenship = self.country,
                  bio = "I am a rising junior",
                  signup_code = "23ey")
        account.owner = user
        account.save()

    def generate_user(self):
        self.generate_random()
        self.get_names()
        user = User(title="Mr.",
                     firstname = self.first_name,
                     lastname= self.last_name,
                     email= self.first_name+self.last_name+"@gmail.com"
                     ).save()
                     
        account = Account(username=self.first_name+self.last_name,
                  email=self.first_name+self.last_name+"@gmail.com",
                  password="17ROW1992",
                  phone = self.phone,
                  department = "School of Informatics and Computing",
                  institution = self.inst,
                  adviser_contact = "Bloomington, Indiana",
                  institute_address = self.city,
                  institute_country = self.country,
                  url = "www.google.com",
                  citizenship = self.country,
                  bio = "I am a rising junior",
                  signup_code = "23ey")
        account.owner = user
        account.save()
        
        
    def delete_all(self):
        for account in Account.objects:
            account.delete()
        print "\n"
        print 70 * "-"
        print "\n\t\t***All Accounts Deleted*** \n"
        print 70 * "-"

    def delete_user(self):
    	i = 0
    	for account in Account.objects:
    	    if i < self.p:
        	account.delete()
        	i = i + 1
            else:
            	break

    def delete_account(self, name):
        for account in Account.objects:
    	    if account.owner.firstname == name:
    		account.delete()

    def find_user(self, name):
        #print
        #Account.objects(firstname = name).count()
        #print count
        print "\nLIST OBJECTS"
        print 70 * "-"
        print
        for account in Account.objects:
    	    if account.owner.firstname == name:
    	    	print
    		print account.owner.firstname, ":", account
    		print
        print "\n" + 70 * "-"

    def find_all(self):
        print "\nLIST OBJECTS"
        print 70 * "-"
        print

        for account in Account.objects:
            print
            print account.owner.firstname, ":", account
            print

        print "\n" + 70 * "-"

if __name__ == '__main__':
    #try:
    c = generate_random_user()
    
    arguments = docopt(__doc__)
        
    if(arguments["gen"]):
    	if(arguments["rand"]):
    		for i in range(c.p):
    			c.generate_user()
    	elif(arguments["--num"]):
    		c.p = int(arguments['--num'])
    		for i in range(c.p):
    			c.generate_user()
    elif(arguments["add"]):
    	if(arguments["--line"]):
    		info = arguments['--line']
    		c.user_info = info.split('/')
    		c.city = raw_input('City: ')
    		c.phone = raw_input('Phone number: ')
    		c.inst = raw_input('Institution: ')
    		c.country = raw_input('Country: ')
    	elif(arguments["--file"]):
    		user_file = arguments["--file"]
    		with open(user_file, 'r') as f:
    			doc = yaml.load(f)
    		c.user_info = doc['user']
    	c.add_user()
    elif (arguments["del"]):                                      
    	if(arguments["all"]):
    		c.delete_all()
    	elif(arguments["--user"]):
    		user = arguments['--user']
    		c.delete_account(user)
    	elif(arguments["--num"]):
    		c.p = int(arguments['--num'])
    		c.delete_user()
    elif(arguments["find"]):
    	if(arguments["all"]):
    		c.find_all()
    	elif(arguments["--user"]):
    		user = arguments['--user']
    		c.find_user(user)
            
    #except DocoptExit as e:
     #   print e.message


#def print_contacts(columns):
    #pass

#print_contacts(["username", "phone", "email"])

#print_summary()

"""how many users from bloomington
how many from chicago
mhao many for that isntitue"""

   
