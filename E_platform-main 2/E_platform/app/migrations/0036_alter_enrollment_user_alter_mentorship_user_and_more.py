# Generated by Django 4.1.4 on 2024-05-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0035_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.AlterField(
            model_name="mentorship",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.DeleteModel(
            name="Admin",
        ),
    ]
