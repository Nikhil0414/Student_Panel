# Generated by Django 5.0.6 on 2024-06-05 16:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0085_mentorship_delete_mentorshiprequest"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Mentorship",
        ),
    ]
