from django.db import models


class Courses_names(models.Model):
  title = models.CharField('Название', max_length=50)
  description_text = models.TextField('Описание', default='Описания нет')
  picture_url = models.CharField('Ссылка на обложку', default='static/main/img/noimage_detail.png', max_length=1000)
  courses_url = models.CharField('Ссылка на основную страницу', default='courses', max_length=1000)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Название курса'
    verbose_name_plural = 'Название курсов'
    db_table = 'course_name'


class Course_articles(models.Model):
  article_title = models.CharField('Название статьи', max_length=50)
  course_name = models.ForeignKey(Courses_names, on_delete=models.CASCADE)
  article_url = models.CharField('Ссылка на статью', default='home_course', max_length=1000)

  def __str__(self):
    return self.article_title

  class Meta:
    verbose_name = 'Статья курса'
    verbose_name_plural = 'Статьи курсов'
    db_table = 'course_article'


class Course_articles_modulues(models.Model):
  module_title = models.CharField('Название заголовка', max_length=50)
  course_article = models.ForeignKey(Course_articles, on_delete=models.CASCADE)
  picture_url = models.CharField('Ссылка на рисунок', blank=True, max_length=1000)
  picture_description = models.CharField('Название рисунка', blank=True, max_length=1000)
  video_url = models.CharField('Ссылка на видео', blank=True, max_length=1000)
  module_text = models.TextField(blank=True)

  def __str__(self):
    return self.module_title

  class Meta:
    verbose_name = 'Глава статьи'
    verbose_name_plural = 'Главы статьей'
    db_table = 'article_module'

class Course_article_lists(models.Model):
  arcticle_module = models.ForeignKey(Course_articles_modulues, on_delete=models.CASCADE)
  item_text = models.TextField()

  def __str__(self):
    return self.item_text

  class Meta:
    verbose_name = 'Список'
    verbose_name_plural = 'Списки'
    db_table = 'module_list'
