# Generated by Django 5.0.4 on 2024-04-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
