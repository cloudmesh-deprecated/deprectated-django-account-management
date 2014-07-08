Python Preparation 
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

Please activate it with::

  source ~/ENV/bin/activate

.. note::
	If errors come while installing the distribute_setup.py, go to pypi.python.org and download the most recent distribute package. 
	In this case, it would be https://pypi.python.org/pypi/distribute/0.6.49 
	. Then do a ``cd distribute-0.6.49`` and then ``python distribute_setup.py`` 
	
	Also to make sure you have universe type the following command in the 
	terminal
	
	``sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu$(lsb_release -sc) universe"``
	


