# Generated by Django 4.0.4 on 2022-05-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='people',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]
