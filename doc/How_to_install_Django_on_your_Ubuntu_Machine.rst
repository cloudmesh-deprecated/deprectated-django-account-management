How to Install Django on Ubuntu Machine:

1. Install python on Ubuntu Machine (if you haven't already)
	sudo apt-get install python 
   *After entering command type python and you should get the following prompt:


 

2. Install pip on Ubuntu Machine (if you haven't already)
	sudo apt-get install python-pip
    *If you get “E: Unable to locate package python-pip” message then you will have to download python distribute package. 

Following these next steps:
Go to pypi.python.org and download the most recent distribute package (https://pypi.python.org/pypi/distribute/0.6.49)

Then extract the download into your desktop 
Go into terminal (make sure you're in root) and then go to Desktop directory

cd distribute-0.6.49

python distribute_setup.py

Ensure easy_install is installed run the following commands:

which easy_install

(a typical response after hitting enter or return would be: /usr/local/bin/easy_install)

Now, pip can be installed by following the command below:
sudo easy_install pip

3. Install Virtualenv on Ubuntu Machine (if you haven't already)
        sudo pip install --upgrade virtualenv

4. Install SQLite on Ubuntu Machine (if you haven't already)
Go to www.sqlite.org/download.html and download the sqlite-shell-linux
Extract download to your respective directory 

	
5. Execute the following commands in the terminal (for some commands user might need to be in root):
         sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe”



6. Make a django directory and then install django
       
	pip install django
	exit
	

      You should be able to type in python and type import django and get the following



7.  The type the following while in the $ directory:
       
	django-admin.py startproject mysite 
        cd mysite
        python manage.py runserver
        
8. After connecting to server
	
	Ctrl C
	python manage.py syncdb
	python manage.py runserver
	
9. On server page
	/admin on the url and login to your server

