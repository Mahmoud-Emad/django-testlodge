# Generated by Django 4.0.4 on 2022-05-14 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0014_alter_people_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='testplan',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_test_plans', to='test_tracker.project'),
        ),
    ]
