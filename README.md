<h1>Pizza</h1>

<p>
Pizza is the third project of the CS50W course: an online takeaway service based on the menu of the popular Pinochio’s Pizza in Cambridge MA (<a href="https://www.pinocchiospizza.net/menu.html">https://www.pinocchiospizza.net/menu.html</a>). Site visitors can view the restaurant menu, log in, place orders for food and view their historic orders. As a personal touch, the site also allows restaurant staff to view and complete orders that have been placed by users, and manage the menu via admin accounts. 
</p>
<h2>Django</h2>


<p>
The site is built using the Django web framework - it includes a huge number of pre-implemented tools out of the box, that take care of a lot of the more common features of a web application for you. These include:
</p>
<ul>

<li>User authentication and security

<li>Database creation/management and ORM

<li>HTML templating

<li>Site Administration through a web based GUI or “admin interface”
</li>
</ul>
<p>
And much more…
</p>
<h2>Django Project Structure</h2>


<p>
Django projects follow a strict convention that facilitates the use of the django toolkit, and more generally adds a semblance of logic and organisation to your working environment. Sites built in django are viewed as a collection of web applications that are grouped together to form a single “project”. 
</p>
<p>
All Django apps begin with a file called manage.py and your “project” folder named after your project (so in this case “pizza”), like so:
</p>

<pre><code>
manage.py
pizza/
	__init__.py
	settings.py
	urls.py
	wsgi.py

</pre></code>

<p>
<code>manage.py</code> contains the wherewithal to interact with your project via the command line - it’s the workhorse that allows you to run your development server, set up your database and database schema, run a python shell within your project environment and loads more. For example, typing:
</p>
<p>
	
<pre><code>
>>> Python manage.py runserver
</code></pre>

</p>
<p>
as you might expect, instructs Django to start a development server.
</p>
<p>
The files in the <code>pizza/</code> directory form the python “package” for your project; this is specified by <code>__init__.py</code> - this tells python that the directory is to be considered a python package, and allows other scripts to refer to the files in the package using “dotted module names”, for example <code>pizza.urls</code> refers to the contents of the <code>urls.py</code> file. 
</p>
<p>
The other files contain information that tells Django how you want your site to work:
</p>
<ul>

<li><b><code>settings.py</code></b> (unsurprisingly) sets the global settings for your Django project. 

<li><b><code>urls.py</code></b> declares all the different URLs from which clients can request information from your site - this can be thought of like the section headings for the contents page of your site. 

<li><b><code>wsgi.py</code></b> is an entry point for WSGI-compatible servers, not relevant for this project. 
</li>
</ul>
<h2>Apps </h2>

 to create staff accounts without poking around behind the scenes).
</p>
<p>
Load_db.py in turn calls two different functions - load_menu and load_su. These functions are found in the menu and accounts packages respectively, as they involve loading models contained within these applications
</p>
<h2>Dockerfile</h2>


<p>
Included in the root directory is a file storing the settings / instructions for a platform called Docker. To paraphrase significantly, docker creates containers inside which you can run processes. A container is a tiny instance of a computer / server, in which only the requirements for your project are installed and uploaded. In the case of pizza, the Dockerfile instructions tell Docker to add:
</p>
<ul>

<li>A python 3 environment

<li>The packages specified in requirements.txt (e.g. Django)

<li>The files from the pizza root directory
</li>
</ul>
<p>
Once these are loaded into the container, the instructions also tell Docker to call the Django functions to create the site database migrations, and to call the load_db function above to load all the menu/su information into the database. Using these instructions, anybody with Docker installed is able to instantly create and run a pizza server, without having to worry about the requirements of their specific system.
</p>
<h2>Testing / travis.yml</h2>


<p>
Each app package also contains a tests.py file that includes a number of test scripts intended to verify that the site is working as it’s supposed to. Test functions mimic various use cases of the site, and check to ensure that the responses match those expected. Such scripts are particularly useful during development, as developers can quickly verify that changes to the site haven’t broken any other site features downstream. 
</p>
<p>
An extension to this idea of automated testing is the concept of Continuous Integration (CI) - the practice of streamlining updates to a project. The root directory includes a .travis.yml file that ‘speaks’ to a continuous integration service called Travis CI. In the case of Pizza, Travis.ci automatically runs the test scripts for each app every time a commit is pushed to Github. Travis then automatically notifies authors of the status of their commits - i.e. if the changes have caused any of the tests to fail or not. 
</p>
<p>
Applications are the functional elements of your site - they can be distinguished as pieces of reusable functionality, such as a login/logout account management facility or a generic blog collection. When you begin adding features to your project, you do so by telling django to create a new app, which creates a new directory as follows:
</p>
<p>
new_app/
</p>
<p>
	__init__.py
</p>
<p>
	admin.py
</p>
<p>
	apps.py
</p>
<p>
	migrations/
</p>
<p>
		__init__.py
</p>
<p>
	models.py
</p>
<p>
	tests.py
</p>
<p>
	views.py
</p>
<p>
These files are:
</p>
<ul>

<li>__init__.py as before, this tells python that your app is to be considered a package

<li>admin.py allows you to choose the elements of your database model that you would like to be added to django’s admin interface - more on this later

<li>apps.py contains a configuration class for your app - this is to be added to settings.py in your project directory to tell django to include this app in your project and use the project’s settings in this app

<li>migrations/ is part of django’s database management/ORM functionality and is handled by Django

<li>models.py details all of the database models Django will use for ORM relating to your app. Models are represented by Python classes with class variables and methods and are used to store/manipulate/interact with the information in your database

<li>tests.py allows you to create automated test scripts that can be used to check your app is functioning properly after making changes in development- more on this later

<li>urls.py as before, declares the url’s specific to your app. This can be thought of as the contents for each section of your site (not created by default for some reason, but required if your app accepts web requests)

<li>views.py contains the ‘views’ (unsurprisingly) for your app. Views are the functional elements of your app and tell your server what to do when it gets different web requests and how to respond to different events
</li>
</ul>
<p>
For applications that display their own web pages, static/ and templates/ folders are also present, that contain all the static script (CSS/JS etc.) and HTML templates required to display said pages. 
</p>
<p>
Following is a brief description of each of the apps that forms the pizza project and any particularly notable features:
</p>
<h2>Accounts</h2>


<p>
This app is responsible for managing the user account registration / login / logout process for the site. Implementation of such an app is made trivial by Django’s ‘auth’ features available out of the box. These include a  ‘User’ class and an ‘authenticate()’ function: the former containing all the information you would expect of a user account, and the latter managing the users authentication on login. The app has two basic pages: a login page and a register page, both of which are self explanatory.
</p>
<p>
The app’s User class is separated into staff and non staff accounts - these dictate which parts of the site users see when logged in - more on this later.
</p>
<p>
The accounts package also includes a load_su.py function. This is a basic script that creates an admin User account and loads it into the database when the app is first created. Again, more on this later. 
</p>
<h2>Menu</h2>


<p>
When users first visit the site, they are presented with the Pinochio’s menu, which is managed by this app. The bulk of the content in this app is found in models.py; this defines the three database models that comprise the items on the menu: 
</p>
<ul>

<li>MenuDIsh, the overall category the dish falls into i.e. Pizzas, Subs, Pasta

<li>MenuItem, the specific item within the dish category i.e. 10” Pizza, Meatball Sub

<li>MenuExtra, extras that can be added to certain items on the menu
</li>
</ul>
<p>
The MenuItem and MenuExtra classes include foreign keys relating to the dishes and items respectively that they are associated with. Also featured are class methods used by other parts of the project to render information from the different class entries in the database.
</p>
<p>
A load_menu.py script is included that takes the data in the Pinochio’s menu and loads it into the database when called - more later. 
</p>
<p>
views.py takes all of the associated information from the database and renders it on the menu page - this means any changes made to the menu in the database are automatically reflected, rather than needing to be hard-coded on a static page. Django has it’s own templating language (very similar to Jijnja) which takes information directly from the context variable passed from the views script, and renders it on the page when referenced. 
</p>
<h2>Orders</h2>


<p>
The orders app handles all of the functionality of the site, allowing registered users to place orders from the menu. Users can open an order, add items to the order specifying any extras, edit their order items, pay for an order and view historic orders.
</p>
<p>
Two new database models are used to store user order information - Order and OrderItem. Each Order has a many-to-many association with a number of OrderItems, and each order item is associated with a MenuItem via a foreign key. The Models also include a number of methods that help facilitate the different app views and the information that is displayed on the associated pages.
</p>
<p>
Views.py again renders information from the menu for users to choose from. It also updates user orders in the database as and when they choose items, and displays historic orders that users have paid for.
</p>
<h2>Kitchen</h2>


<p>
<strong><em>Personal touch - this is functionality not specified in the project brief</em></strong>
</p>
<p>
This can be thought of as the other face of the Orders app, that restaurant staff use to view orders that customers have placed. Users with an is_staff flag will be redirected to the Kitchen app - this changes the look of the site slightly and offers users the ability to view all open orders and completed orders - displaying all the customer orders that haven’t been marked complete and those that have been completed respectively.
</p>
<p>
The functionality of this section of the app is very similar to elements of the menu and orders apps. The menu is displayed in a very similar way to the ordinary user site (with possible future updates allowing menu editing directly on this page) and the current / historic orders sections are very similar to the historic orders section of the ordinary site, but allow staff to mark orders as completed - this information is then displayed on the respective user’s orders. 
</p>
<h2>Admin</h2>


<p>
One of the key tools that Django provides is it’s admin interface. This allows site administrators (superusers) the ability to change the information in the site database via a GUI, which can be accessed at /admin. Each separate app package includes an admin.py file that specifies the models from the app that should be added to the admin interface.
</p>
<p>
In the case of Pizza, site admins can add / change / delete items from the menu, the details of customers orders and the different user accounts (including adding staff privileges to an account).
</p>
<h2>load_db</h2>


<p>
Additional to the default files in the pizza package is a file called load_db.py. This automates the process of adding all the information to the database that is required for the site to run properly i.e. the menu information and a superuser account (as otherwise it would not be possible to create staff accounts without poking around behind the scenes).
</p>
<p>
Load_db.py in turn calls two different functions - load_menu and load_su. These functions are found in the menu and accounts packages respectively, as they involve loading models contained within these applications
</p>
<h2>Dockerfile</h2>


<p>
Included in the root directory is a file storing the settings / instructions for a platform called Docker. To paraphrase significantly, docker creates containers inside which you can run processes. A container is a tiny instance of a computer / server, in which only the requirements for your project are installed and uploaded. In the case of pizza, the Dockerfile instructions tell Docker to add:
</p>
<ul>

<li>A python 3 environment

<li>The packages specified in requirements.txt (e.g. Django)

<li>The files from the pizza root directory
</li>
</ul>
<p>
Once these are loaded into the container, the instructions also tell Docker to call the Django functions to create the site database migrations, and to call the load_db function above to load all the menu/su information into the database. Using these instructions, anybody with Docker installed is able to instantly create and run a pizza server, without having to worry about the requirements of their specific system.
</p>
<h2>Testing / travis.yml</h2>


<p>
Each app package also contains a tests.py file that includes a number of test scripts intended to verify that the site is working as it’s supposed to. Test functions mimic various use cases of the site, and check to ensure that the responses match those expected. Such scripts are particularly useful during development, as developers can quickly verify that changes to the site haven’t broken any other site features downstream. 
</p>
<p>
An extension to this idea of automated testing is the concept of Continuous Integration (CI) - the practice of streamlining updates to a project. The root directory includes a .travis.yml file that ‘speaks’ to a continuous integration service called Travis CI. In the case of Pizza, Travis.ci automatically runs the test scripts for each app every time a commit is pushed to Github. Travis then automatically notifies authors of the status of their commits - i.e. if the changes have caused any of the tests to fail or not. 
</p>
