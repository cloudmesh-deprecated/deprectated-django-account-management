management
==========

Install Mongodb
----------------------------------------------------------------------

To do figure out if the sudo is needed

::

  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
  sudo apt-get update
  sudo apt-get install mongodb-org
  sudo apt-get install mongodb-org=2.6.1 mongodb-org-server=2.6.1 mongodb-org-shell=2.6.1 mongodb-org-mongos=2.6.1 mongodb-org-tools=2.6.1
  sudo /etc/init.d/mongod start
  start mongod
  sudo start mongod
  ps -aux
  less /var/log/mongodb/mongod.log
  sudo /etc/init.d/mongod stop
  service mongod stop
  sudo service mongod stop
  ps -aux
  history


Start mongo as user
----------------------------------------------------------------------

  mongod --dbpath .

Mongoengine
----------------------------------------------------------------------

::

   pip install mongoengine

Test
----------------------------------------------------------------------

::
  from mongoengine import *

  connect('user')

  class User(Document):
      firstname = StringField()
      lastname = StringField()

      def __str__(self):
	  return "{0} {1}".format(self.firstname, self.lastname)



  user = User(firstname="Gregor", lastname="von Laszewski")
  user.save()

  user = User(firstname="Fugang", lastname="Wang")
  user.save()

  print
  print "LIST OBJECTS"
  print 70 * "-"

  for user in User.objects:
      print user.firstname, ":",  user

  print
  print "FIND OBJECTS"
  print 70 * "-"

  users = User.objects(firstname="Gregor")

  for user in users:
      print user.firstname, ":", user

