# Generated by Django 4.1.4 on 2024-05-15 17:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0058_alter_course_this_course_includes_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="grade",
        ),
    ]
