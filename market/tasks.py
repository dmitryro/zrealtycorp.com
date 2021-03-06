from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from periodically.decorators import *
import datetime
import celery

@hourly()
def my_task():
    print 'Do something!'

@every(minutes=1)
def my_other_task():
    print 'Do something else every  minutes!'

 
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

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=3))
def notify():
        id = 1
        name = 'ZRealty System'
        email = 'dmitryro@gmail.com'
        phone = '718 404 6471'
        title = 'System health check'
        mess = 'We are still up and running'


        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = profile.email
        TO = profile.email
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server


        BODY='<html><body><strong>ID</strong> %s'%id
        BODY+='</strong><br/><strong>TITLE</strong> %s'%title
        BODY+='</strong><br/><strong>NAME</strong> %s'%name
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%email
        BODY+='</strong><br/><strong>PHONE</strong> %s'%phone
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        BODY+='</strong></body></html>'

        SUBJECT = 'ZRealtyCorp Inquiry %s'%id
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
            Your mail reader does not support the report format.
            Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)

        msg = MESSAGE.as_string()

        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()

