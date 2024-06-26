# Generated by Django 4.1.4 on 2024-05-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0053_student_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="wishlist",
            field=models.ManyToManyField(
                related_name="students_in_wishlist", to="app.course"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="EmailID",
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="Full_Name",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="Mobile_no",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="cart",
            field=models.ManyToManyField(
                related_name="students_in_cart", to="app.course"
            ),
        ),
    ]
