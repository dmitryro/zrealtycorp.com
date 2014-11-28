ZRealty Corp Apartment Listing project.

======================================================================================================

This project is built with Django 1.6, DRF and Python 2.7.8

1. Django 1.65
2. DRF
3. AngularJS
4. Bower
5. Grunt
6. Node.js

======================================================================================================

Models: 
---------
1. Agent
2. Borough
3. Cateogory
4. Icon
5. Neighborhood
6. Page
7. Property
8. Role
9. Status 

======================================================================================================
STARTING THE APPICLATION
------------------------

1. Configure uwsgi with nginx and create a cluster on ports 8001 8002 8003 8004 8005
2. sudo bower install angular-django-rest-resource  --allow-root
4. sudo npm install grunt
5. sudo npm install grunt-contrib-coffee
6. sudo grunt
7. copy the last static files located in static_files dir by running
   python2.7 manage.py collectstatic
8. python2.7 manage.py syncdb --migrate
9. run bash start.sh or run the following command from the project's root directory:
   <br/>
   uwsgi --socket :8001 --module zrealty.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:8181 --daemonize=/var/www/vhosts/zrealtycorp.com/logs/uwsg.log
   <br/>


10. View the current live site at http://zrealtycorp.com


=====================================================================================================
This README document is a draft version and is subject to permanent updates.
The project inteneded to be a searchable Real Estate apartment list.



