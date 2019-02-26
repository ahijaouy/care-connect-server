# Generated by Django 2.1.7 on 2019-02-26 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('description', models.TextField(max_length=250)),
                ('img_url', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=250)),
                ('date', models.DateTimeField()),
                ('caretaker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Caretaker')),
            ],
        ),
        migrations.CreateModel(
            name='Elderly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('elderly', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Elderly')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('q1', models.TextField(max_length=250)),
                ('q2', models.TextField(max_length=250)),
                ('q3', models.TextField(max_length=250)),
                ('q4', models.TextField(max_length=250)),
                ('caretaker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Caretaker')),
                ('elderly', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Elderly')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='elderly',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Elderly'),
        ),
        migrations.AddField(
            model_name='activity',
            name='activityType',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='caretaker',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Caretaker'),
        ),
        migrations.AddField(
            model_name='activity',
            name='elderly',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.Elderly'),
        ),
    ]