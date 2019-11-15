# Project 3

Pizza is an online takeaway service based on the menu of the popular Pinochio’s Pizza in Cambridge MA ([https://www.pinocchiospizza.net/menu.html](https://www.pinocchiospizza.net/menu.html)). Users can view the restaurant menu, log in, place orders for food and view their historic orders. The site also allows restaurant staff to view orders and manage the menu via admin accounts. 

## Django

The site is built using the Django web framework - it includes a huge number of pre-implemented tools “out of the box“ that take care of a lot of the more common features of a web application for you, including:



*   User authentication and security
*   Database creation/management and ORM
*   HTML templating
*   Site Administration through a web based GUI or “admin interface”

And much more…


## Django Project Structure

Django projects follow a strict convention that facilitates the use of the django toolkit, and more generally adds a semblance of logic and organisation to your working environment. Sites built in django are viewed as a collection of web applications that are grouped together to form a single “project”. 

All Django apps begin with a file called manage.py and your “project” folder named after your project (so in this case “pizza”), like so:

manage.py

pizza/

	__init__.py

	settings.py

	urls.py

	Wsgi.py

Manage.py contains the wherewithal to interact with your project via the command line - it’s the workhorse that allows you to run your development server, set up your database and database schema, run a python shell within your project environment and loads more. For example, typing:

Python manage.py runserver

As you might expect, instructs Django to start a development server.

The files in the ‘pizza’ directory form the python “package” for your project; this is specified by the __init__.py file at the top of the folder - this tells python that the folder is to be considered a python package, and allows other scripts to refer to the files in the package using “dotted module names”, for example ‘pizza.urls’ refers to the contents of the urls.py file. 

The other files contain information that tells Django how you want your site to work:



*   settings.py (unsurprisingly) sets the global settings for your Django project. 
*   urls.py declares all the different URLs from which clients can request information from your site - this can be thought of like the section headings for the contents page of your site. 
*   wsgi.py is an entry point for WSGI-compatible servers, not relevant for this project. 


## Apps 

Applications are the functional elements of your site - they can be distinguished as pieces of reusable functionality, such as a login/logout account management facility or a generic blog collection. When you begin adding features to your project, you do so by telling django to create a new app, which creates a new directory as follows:

new_app/

	__init__.py

	admin.py

	apps.py

	migrations/

		__init__.py

	models.py

	tests.py

	views.py

These files are:



*   __init__.py as before, this tells python that your app is to be considered a package
*   admin.py allows you to choose the elements of your database model that you would like to be added to django’s admin interface - this allows site admin’s to manipulate information in the database via a GUI
*   apps.py contains a configuration class for your app - this is to be added to settings.py in your project directory to tell django to include this app in your project and use the project’s settings in this app
*   migrations/ is part of django’s database management/ORM functionality and is handled by Django
*   models.py details all of the database models Django will use for ORM relating to your app. Models are represented by Python classes with class variables and methods and are used to store/manipulate/interact with the information in your database
*   tests.py allows you to create automated test scripts that can be used to check your app is functioning properly after making changes in development- more on this later
*   urls.py as before, declares the url’s specific to your app. This can be thought of as the contents for each section of your site (not created by default for some reason, but required if your app accepts web requests)
*   views.py contains the ‘views’ (unsurprisingly) for your app. Views are the functional elements of your app and tell your server what to do when it gets different web requests and how to respond to different events

Following is a brief description of each of the apps that forms the pizza project and any particularly notable features:


## Accounts

This app is responsible for managing the user account login / logout process for the site. 


## Kitchen


## Menu


## Orders
