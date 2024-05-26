# Generated by Django 5.0.4 on 2024-04-30 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_quizresult_quiz_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='marked',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AssignmentFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('marks', models.FloatField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]