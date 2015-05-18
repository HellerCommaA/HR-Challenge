from datetime import timedelta, datetime
from celery import Celery
from app import db
import os
import sqlalchemy
from app.models import *

from secret import AWSID, AWSPW
basedir = os.path.abspath(os.path.dirname(__file__))

 
app = Celery('page_saver')
app.conf.update(
    # BROKER_URL='sqla+sqlite:///' + os.path.join(basedir, 'celerydb.sqlite'),
    BROKER_URL = 'sqs://' + AWSID + ':' + AWSPW + '@',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYBEAT_SCHEDULE={
        'save_page':{
            'task':'page_saver.save_page',
            'schedule': timedelta(hours = 2)
        }
    }
)
 
from random import randint
@app.task(name='page_saver.save_page')
def save_page():
	# faker = Faker()
	f = FakeData(rand = randint(1,50), time = datetime.now())
	db.session.add(f)
	db.session.commit()
	del f