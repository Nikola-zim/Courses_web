# Generated by Django 4.1.2 on 2022-12-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_alter_courses_names_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="courses_names",
            name="courses_url",
            field=models.CharField(
                default="home_course",
                max_length=1000,
                verbose_name="Ссылка на основную страницу",
            ),
        ),
    ]
