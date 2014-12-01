ZRealty Corp Apartment Listing project.

======================================================================================================

This project is built with Django 1.7.1, DRF and Python 2.7.8

1. Django 1.7
2. DRF
3. AngularJS

======================================================================================================
Motivation
----------
The project provides out of the box RESTful Real Estate Listing feauturing useful functionality tools
such as
<br/>
1. Publishing categorized properties into RESTful listing
2. Search properties usingi search filters
3. Per property reach back functionality - <br/>
   - allowing to contact the publisher on a per property base
   - allowing to focus on processing specific published proceprty
   - allowing to satify requests on a per item base
4. Customer Dashboard
   - allowing a registered customer to keep track of their data
   - allowing a registered customer publish properties or blog tweets
5. Social Authentication and registration for customers using Django's social_auth


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



