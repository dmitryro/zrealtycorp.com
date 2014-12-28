import logging
import logging.handlers
import daemon
import os
import urllib2
from celery import Celery

with daemon.DaemonContext():
    if __name__ == "__main__":
        app = Celery('tasks', broker='redis://localhost:6379/0')

        @app.task
        def add(x, y):
            return x+y
