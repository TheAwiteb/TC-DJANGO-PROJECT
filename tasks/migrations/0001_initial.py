# Generated by Django 4.1 on 2022-08-04 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("teams", "0001_initial"),
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(help_text="Task title", max_length=55)),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Todo", "Todo"),
                            ("In progress", "Inprogress"),
                            ("Completed", "Completed"),
                        ],
                        help_text="Task status",
                        max_length=40,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Task creation date"
                    ),
                ),
                (
                    "completed_at",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="Task completion date",
                        null=True,
                    ),
                ),
                (
                    "assignees",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Assignees",
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="organization.organization",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tasks",
                        to="teams.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewRequest",
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
                ("content", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_requests",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                (
                    "approved",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the review request was approved",
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        help_text="The content of the change request",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "request",
                    models.ForeignKey(
                        help_text="The review request",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="tasks.reviewrequest",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
    ]