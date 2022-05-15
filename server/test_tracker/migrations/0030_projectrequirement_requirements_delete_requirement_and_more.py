# Generated by Django 4.0.4 on 2022-05-15 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0029_alter_people_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_requirements', to='test_tracker.project')),
            ],
            options={
                'verbose_name': 'Requirement',
                'verbose_name_plural': 'Requirements',
            },
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_requirement', to='test_tracker.requirements'),
        ),
    ]
