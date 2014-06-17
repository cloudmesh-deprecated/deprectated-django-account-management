from management import User
from management import Account
from user_dict import names
import random

from mongoengine import *

# https://code.google.com/p/prettytable/
# https://code.google.com/p/prettytable/source/browse/trunk/README

connect ('user')#, port=27777)

"This class generates random users"

class generate_random_user():
    
    first_name = "abc"
    last_name = "abc"
    
    def generate_firstname(self):
        num1 = random.randint(0,4)
        return names[num1]

    def generate_lastname(self):
        num2 = random.randint(0,4)
        return names[num2]
    
    def get_names(self):
        self.first_name = self.generate_firstname()
        self.last_name = self.generate_lastname()

    def generate_user(self):
        self.get_names()
        user = User(title="Mr.",
                     firstname = self.first_name,
                     lastname= self.last_name,
                     email= self.first_name+self.last_name+"@gmail.com").save()
                     
        account = Account(username=self.first_name+self.last_name,
                  email=self.first_name+self.last_name+"@gmail.com",
                  password="17ROW1992")
        account.owner = user
        account.save()
        
        
    def delete_all_users(self):
        accounts = Account.objects()
        for account in Account.objects:
            account.delete()

    def print_users(self):
        self.generate_user()
        print "\nLIST OBJECTS"
        print 70 * "-"
        print

        accounts = Account.objects()

        for account in accounts:
            print account.owner.firstname, ":", account

        print "\n" + 70 * "-"

c = generate_random_user()
c.print_users()

def print_contacts(columns):
    pass

print_contacts(["username", "phone", "email"])

#print_summary()

"""how many users from bloomington
how many from chicago
mhao many for that isntitue"""

   