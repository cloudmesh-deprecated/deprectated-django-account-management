import yaml
from mongoengine import *
import datetime, time
import hashlib, uuid
import yaml
from pprint import pprint
from user import User, Users

connect('user', port = 27777)

users = Users()

#Reads user information from file

def add_user():
    user = users.read("user_info.yaml")

    print user

    data = User(
            title = user['title'],
            firstname = user['firstname'],
            lastname = user['lastname'],
            email = user['email'],
            username = user['username'],
            active = True,
            password = user['password'],
            phone = user['phone'],
            department = user['department'],
            institution = user['institution'],
            address = user['address'],
            country = "USA",
            citizenship = "US",
            bio = user['bio'],
        )

    users.add(data)
    
if __name__ == "__main__":
    main()
