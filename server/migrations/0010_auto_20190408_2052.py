# Generated by Django 2.1.7 on 2019-04-08 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_remove_quizresponse_q7_appetite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizresponse',
            old_name='q7_appetite_new',
            new_name='q7_appetite',
        ),
    ]