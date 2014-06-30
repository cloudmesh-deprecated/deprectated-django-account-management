PWD=`pwd`
PROJECT=`basename \`pwd\``

all:
	echo $(PROJECT)

create:
	mkdir $(PROJECT)
	cd $(PROJECT); django-admin.py startproject $(PROJECT)

start:
	python manage.py syncdb
	python manage.py runserver

stop:
	killall python

view:
	open http://127.0.0.1:8000/

clean:
	rm *.sqlite3
