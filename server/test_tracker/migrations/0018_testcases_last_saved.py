# Generated by Django 4.0.4 on 2022-05-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("test_tracker", "0017_rename_req_tc_title_project_req_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="testcases",
            name="last_saved",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="last_saved_test_cases",
                to="test_tracker.member",
            ),
        ),
    ]
