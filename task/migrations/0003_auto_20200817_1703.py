# Generated by Django 3.1 on 2020-08-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_redis_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='redis_id',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='id redis'),
        ),
    ]
