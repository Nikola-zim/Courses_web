# Generated by Django 4.1.2 on 2022-12-17 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0009_course_articles_article_url_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course_articles_modulues",
            options={
                "verbose_name": "Глава статьи",
                "verbose_name_plural": "Главы статьи",
            },
        ),
        migrations.AlterField(
            model_name="course_articles",
            name="course_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.courses_names"
            ),
        ),
        migrations.AlterField(
            model_name="course_articles_modulues",
            name="course_article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.course_articles",
            ),
        ),
        migrations.CreateModel(
            name="Course_article_lists",
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
                ("item_text", models.TextField()),
                (
                    "arcticle_module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course_articles_modulues",
                    ),
                ),
            ],
            options={
                "verbose_name": "Список",
                "verbose_name_plural": "Списки",
                "db_table": "module_list",
            },
        ),
    ]
