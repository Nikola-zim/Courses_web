# Generated by Django 4.1.2 on 2022-12-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_courses_names_courses_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses_names",
            name="picture_url",
            field=models.CharField(
                default="static/main/img/noimage_detail.png",
                max_length=1000,
                verbose_name="Ссылка на обложку",
            ),
        ),
    ]
