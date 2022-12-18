# Generated by Django 4.1.2 on 2022-12-17 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_alter_courses_names_courses_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course_articles",
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
                    "article_title",
                    models.CharField(max_length=50, verbose_name="Название статьи"),
                ),
                (
                    "course_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="courses.courses_names",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья курса",
                "verbose_name_plural": "Статьи курсов",
            },
        ),
        migrations.CreateModel(
            name="Course_articles_modulues",
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
                    "module_title",
                    models.CharField(max_length=50, verbose_name="Название заголовка"),
                ),
                (
                    "picture_url",
                    models.CharField(max_length=1000, verbose_name="Ссылка на обложку"),
                ),
                ("module_text", models.TextField()),
                (
                    "course_article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="courses.course_articles",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подзаголовок статьи",
                "verbose_name_plural": "Подзаголовки статей",
            },
        ),
    ]