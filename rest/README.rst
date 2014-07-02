Simple example
==========================================================

::

   terminal_1> fab db
   terminal_1> fab run 

For the test to run, use the password and username specified whne creating the db

::

   terminal_2> fab test

To view the invormation in the browser you can say::

  terminal_2> fab view

To see the documentation with swagger you can say

  terminal_2> fab doc

To clean things up say

   terminal_2> fab clean

Do not forget to stop your server in terminal 1 with CONTROL^C.



