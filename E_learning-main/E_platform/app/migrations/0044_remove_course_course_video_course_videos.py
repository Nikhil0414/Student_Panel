# Generated by Django 4.1.4 on 2024-05-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0043_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="course_video",
        ),
        migrations.AddField(
            model_name="course",
            name="videos",
            field=models.ManyToManyField(blank=True, to="app.video"),
        ),
    ]
