# Generated by Django 4.0.4 on 2022-05-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0017_remove_testplan_temps_testplan_temps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
