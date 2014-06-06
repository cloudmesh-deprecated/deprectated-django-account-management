from management import User
from management import Account
from management import Contact
from mongoengine import *

# https://code.google.com/p/prettytable/
#  https://code.google.com/p/prettytable/source/browse/trunk/README
# 
#

connect ('user', port=27777)

ifeanyi = User(title="Mr.", firstname="Ifeanyi",
               lastname="Onyenweaku",
               email="rowlandifeanyi17@gmail.com")
ifeanyi.save()

account = Account(username="rowlandifeanyi",
                    email="rowlandifeanyi17@gmail.com",
                    password="17ROW1992")
account.owner = ifeanyi
account.save()

jeff = User(title="Mr.", firstname="Jeffery",
            lastname="Ridgeway",
            email="jeff01@gmail.com")
jeff.save()

account = Account(username="jeff01",
                    email="jeff01@gmail.com",
                    password="17JEFF1992")
account.owner = jeff
account.save()

print
print "LIST OBJECTS"
print 70 * "-"
print

accounts = Account.objects()

for account in accounts:
    print account.owner.firstname, ":", account

print
print 70 * "-"