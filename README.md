======================================================================================================

ZRealty Corp Apartment Listing project.

======================================================================================================

This project is built with Django 1.7.1, DRF and Python 2.7.8

1. Django 1.7.1
2. Django Rest Framework 3.0.1
3. AngularJS 1.3


======================================================================================================
RATIONALE
----------
The project provides out of the box RESTful Real Estate Listing <br/>
feauturing useful functionality tools:<br/>
  1. Publishing categorized properties into RESTful listing:
     - Properties offered for sale. <br/>
     - Properties offered for rent. <br/>
     - Featured properties. 

  2. Search properties using search filters <br/>
     - The filters open by clicking the menu's search icon.<br/>
     - The customer is offered to select one or more criteria to search.<br/>
     - The requested search query acts on top of Django Rest Framework.

  3. Per property reach back functionality - <br/>
     - this feature allows a customer, viewing the details of a specific <br/>
     property, to reach back the publisher immediately using the property ID <br/>
     and customer's reach back info - this invalidates the need of any office <br/>
     calls and makes negotiation focused on a specific published property. <br/>
     - allowing to contact the publisher on a per property base.
     - allowing to focus on processing specific published property.
     - allowing to satify requests on a per item base.<br/>

  4. Customer Dashboard - <br/>
     - if you're a returning customer use http://zrealtycorp.com/signin
       (if deployed on your domain, use http://yourdomain.com/signin to enter
       the Dashboard).
     - if you don't have an account please register a new one by going to
       zrealtycorp.com/signup (if deployed on your domain, use 
       http://yourdomain.com/signup to create a new account). The confirmation
       email will be sent to the email you will provide.
     - allowing a registered customer to keep track of their data
     - a logged in customer can edit his profile
     - a logged in customer can publish properties.<br/>
     - a logged in customer can publish new messages to blog.<br/>
     - a logged in customer can send private messages to another registered
       customers.<br/>

  5. Social Authentication and Registration for customers 
     - utilizing Ouath2 and Django's social_auth. <br/>

  6. Dedicated contact form - <br/>
     - Once viewing details of the specific property you might wish to <br/>
       reach the vendor to discuss possible deal omiting calling or <br/>
       otherwise describing your needs or likes. The draggable contact <br/>
       form (implemented using Angular Draggable module) allows better <br/>
       interativity through keeping the contact focused on specific item.<br/>
       The contact form, once open, will include the property ID as well <br/>
       as description, so the message sent will have all the details the <br/>
       selling or renting party needs for fast and focused negotiation.<br/> 

======================================================================================================
Configuration
-------------
1. The default time is set to EST - you might wish to configure it for your timezone.<br/>
2. The pagination is set to 10 items per page - you might wish to configure it to any other amount.<br/>


======================================================================================================
Models: 
---------
1. Agent
2. Borough
3. Cateogory
4. Icon (general purpose image-link model)
5. Neighborhood (chained to Borough model)
6. Page
7. Property
8. Role
9. Status 
10. Type
11. Room (we need this as we have 0 - studio)
12. Member (dahsboard customer profile)

======================================================================================================
STARTING THE APPICLATION
------------------------
1. Clone the repository into your local server root.
2. Set up your local nginx to point to your domain's location .
3. Install django, setuptools, pip and other relevant modules.
4. Install postgresql version 8 or higher. Make sure your log in creds match what's in zrealty/local_settings.py
5. Create Django admin superuser by running
   python manage.py createsuperuser
6. Run
   python manage.py makemigrations    - to generate migrations
   python manage.py migrate           - to migrate your new models
   python manage.py syncdb            - to sync your tables
   python manage.py collectstatic     - to copy your static files
   to set up your local schema and copy the static files.
9. Run bash start.sh (assuming modifications matching your local configs) 
   or run the following command from the project's root directory:
   
   <br/>
   uwsgi --socket :8001 --module zrealty.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:8181 --daemonize=/var/www/vhosts/yourdomain.com/logs/uwsg.log
   <br/>


10. View the current live site at http://zrealtycorp.com


=====================================================================================================
This README document is a draft version and is subject to permanent updates.
The project inteneded to be a searchable Real Estate apartment list.



