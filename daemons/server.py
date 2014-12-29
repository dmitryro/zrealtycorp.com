import logging
import logging.handlers
import daemon
import os
import urllib2
from celery import Celery

def local_monitor(app):
    state = app.events.State()

    def announce_failed_tasks(event):
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(), ))

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-failed': announce_failed_tasks,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)


with daemon.DaemonContext():
    if __name__ == "__main__":
        app = Celery('tasks', broker='redis://localhost:6379/0')
        local_monitor(app)
        os.system("python manage.py celery worker -E")
        @app.task
        def add(x, y):
            return x+y
