# Generated by Django 4.1.4 on 2024-05-03 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0025_remove_assignment_course_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Tech Courses", "Tech Courses"),
                            ("CBSE Courses", "CBSE Courses"),
                        ],
                        default="Tech Courses",
                        max_length=100,
                    ),
                ),
                ("grade", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="staticfiles/course_images/"
                    ),
                ),
                (
                    "demo_video",
                    models.FileField(
                        blank=True, null=True, upload_to="staticfiles/demo_videos/"
                    ),
                ),
                (
                    "course_video",
                    models.FileField(
                        blank=True, null=True, upload_to="staticfiles/course_videos/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionPaper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("year", models.IntegerField()),
                ("subject", models.CharField(max_length=100)),
                ("file", models.FileField(upload_to="question_papers/")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mentorship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("reason", models.TextField()),
                ("phone_number", models.CharField(max_length=15)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.admin"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.admin"
                    ),
                ),
            ],
        ),
    ]