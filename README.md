Ethics-World
============

This is the term project that Brent Blasingame and I are creating for our ethics class.  It is implemented using Python 3 Django.

Installation
============

To run the app on you machine follow these steps.  This should work for Windows, Linux, and OSX.

Install python3.4.  

Install MySQL

Install pip3

using pip3 install django and mysql-connector-python

In the settings.py file in the django app, change the database password and username to whatever you set up during the installation of MySQL.

Create a database in MySQL called Ethics.  

Go to the directory in the Ethics-World app with the manage.py file and run these commands:

python3 manage.py migrate

python3 manage.py createsuperuser

Now that the environment is setup, you can start the development server with: python3 manage.py runserver
