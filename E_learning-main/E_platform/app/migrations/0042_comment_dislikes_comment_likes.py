# Generated by Django 4.1.4 on 2024-05-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0041_remove_comment_author_remove_post_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]