# Generated by Django 4.0.4 on 2022-05-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0015_testplan_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='testplan',
            name='temps',
            field=models.ManyToManyField(null=True, related_name='temps', to='test_tracker.testplandetail'),
        ),
    ]
