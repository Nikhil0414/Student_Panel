# Generated by Django 5.0.6 on 2024-06-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0077_alter_like_unique_together_remove_like_post_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discussion",
            name="user",
        ),
        migrations.AddField(
            model_name="discussion",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
