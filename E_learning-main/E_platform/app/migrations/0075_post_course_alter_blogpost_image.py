# Generated by Django 5.0.6 on 2024-05-31 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0074_blogpost_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.course",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="staticfiles/blog_images/"
            ),
        ),
    ]
