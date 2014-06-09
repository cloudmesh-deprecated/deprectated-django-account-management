Preparing Machine for Django
======================================

First you need to install python if you not already have it installed::

	sudo apt-get install python 

Next you will have to install pip,if you haven't already installed it::

	sudo apt-get install python-pip

Next we make sure the proper vesrion of distribute is installed::

  curl -O http://python-distribute.org/distribute_setup.py
  python distribute_setup.py

Next we make sure to install pip::

  sudo easy_install pip

Now we install virtualenv::

        sudo pip install --upgrade virtualenv

The next step includes creating a virtual env with ::

   virtualenv ~/ENV

Please activate it with 

  source ~/ENV/bin/activate



