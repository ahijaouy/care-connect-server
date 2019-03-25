# Generated by Django 2.1.7 on 2019-03-25 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20190325_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
