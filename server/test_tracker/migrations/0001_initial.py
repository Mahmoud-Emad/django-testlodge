# Generated by Django 4.0.4 on 2022-05-17 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=70, unique=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("activity", models.JSONField(default=dict)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProjectRequirement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_requirements",
                        to="test_tracker.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Requirements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(default="")),
                (
                    "requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_requirement",
                        to="test_tracker.projectrequirement",
                    ),
                ),
            ],
            options={
                "verbose_name": "Requirement",
                "verbose_name_plural": "Requirements",
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "permission",
                    models.CharField(
                        choices=[
                            ("full_access", "Full access"),
                            ("admin_access", "Admin access"),
                        ],
                        default="full_access",
                        max_length=100,
                    ),
                ),
                ("signature", models.UUIDField(default=uuid.uuid4, null=True)),
                ("invited", models.BooleanField(default=False)),
                ("accepted", models.BooleanField(default=False)),
                (
                    "host_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="host_user_manager",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("test_tracker.user",),
        ),
        migrations.CreateModel(
            name="TestSuites",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_test_suites",
                        to="test_tracker.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TestPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                (
                    "type",
                    models.CharField(
                        choices=[("template", "template"), ("blank", "blank")],
                        default="template",
                        max_length=100,
                    ),
                ),
                ("temps", models.JSONField(default=dict)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_test_plans",
                        to="test_tracker.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TestCases",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(default="")),
                (
                    "test_steps",
                    models.TextField(
                        default="A list of steps to perform along with any sample data."
                    ),
                ),
                (
                    "expected_result",
                    models.TextField(
                        default="Details of what the final result should be."
                    ),
                ),
                ("comments", models.TextField(default="")),
                ("passed", models.BooleanField(default=False)),
                ("failed", models.BooleanField(default=False)),
                ("skipped", models.BooleanField(default=False)),
                ("run", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("", ""),
                            ("not_started", "not started"),
                            ("in_progress", "in progress"),
                            ("completed", "completed"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
                ("completed", models.BooleanField(default=False)),
                (
                    "test_suite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_suite_test_cases",
                        to="test_tracker.testsuites",
                    ),
                ),
                (
                    "verify_requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verifies_requirements",
                        to="test_tracker.requirements",
                    ),
                ),
            ],
            options={
                "verbose_name": "TestCase",
                "verbose_name_plural": "TestCases",
            },
        ),
        migrations.CreateModel(
            name="TestRun",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150)),
                (
                    "test_suites",
                    models.ManyToManyField(
                        related_name="run_suites", to="test_tracker.testsuites"
                    ),
                ),
                (
                    "assigned_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_user",
                        to="test_tracker.member",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="project",
            name="members",
            field=models.ManyToManyField(
                related_name="project_members", to="test_tracker.member"
            ),
        ),
    ]
