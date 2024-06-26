# Generated by Django 5.0.6 on 2024-06-27 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0090_post_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="careerguidancemessage",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="guidance_messages",
                to="app.course",
            ),
        ),
    ]
