kill -9 $(pidof uwsgi)
uwsgi --socket :8005 --module zrealty.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --daemonize=/var/www/vhosts/zrealtycorp.com/logs/uwsg.log
