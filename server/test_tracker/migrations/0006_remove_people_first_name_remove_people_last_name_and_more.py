# Generated by Django 4.0.4 on 2022-05-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0005_remove_user_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='people',
            field=models.ManyToManyField(related_name='project_people', to='test_tracker.people'),
        ),
    ]