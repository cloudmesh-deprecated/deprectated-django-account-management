PWD=`pwd`
PROJECT=`basename \`pwd\``

all:
	echo $(PROJECT)

create:
	django-admin.py startproject $(PROJECT)

start:
	python manage.py syncdb

stop:
	killall python

server:
	python manage.py runserver

view: 
	open http://127.0.0.1:8000

clean:
	rm -f *.sqlite3
	rm -f *.pyc */*.pyc */*/.pyc
static:
	python manage.py collectstatic
