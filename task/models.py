from django.db import models
from datetime import datetime


class Task(models.Model):
    text = models.TextField('Решение')
    time = models.DateTimeField('Время отправки', default=datetime.now)
    status = models.CharField('Статус решения', max_length=30)
    task_id = models.PositiveIntegerField('ID решения', default=0)


