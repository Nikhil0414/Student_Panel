# Generated by Django 4.1.4 on 2024-05-17 05:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0061_course_youtube_link_alter_ticket_attachment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="course_video",
        ),
        migrations.RemoveField(
            model_name="course",
            name="youtube_link",
        ),
    ]
