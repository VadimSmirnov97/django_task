from celery import Celery
from django_task.celery import app
import random
import time


def post_submission(text):
    id = int(time.time() * 1000)
    status = random.choice([*['evaluation'] * 10, 'correct', 'wrong'])

    return id, status


@app.task
def get_submission(id):
    status = random.choice([*['evaluation'] * 10, 'correct', 'wrong'])

    return id, status
