from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
 
 
logger = get_task_logger(__name__)
 
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def send_email():
    logger.info("Start task")
    now = datetime.now()

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def tweet():
    logger.info("Start task")
    now = datetime.now()

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def publish_to_facebook():
    logger.info("Start task")
    now = datetime.now()

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def publish_feed():
    logger.info("Start task")
    now = datetime.now()

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def publish_to_vk():
    logger.info("Start task")
    now = datetime.now()



