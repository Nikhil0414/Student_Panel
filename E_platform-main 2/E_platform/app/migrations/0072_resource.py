# Generated by Django 4.1.4 on 2024-05-24 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0071_careerguidancemessage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
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
                ("title", models.CharField(max_length=100)),
                (
                    "pdf_file",
                    models.FileField(
                        blank=True, null=True, upload_to="staticfiles/week_resources/"
                    ),
                ),
                (
                    "week",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resources",
                        to="app.week",
                    ),
                ),
            ],
        ),
    ]
