from django.shortcuts import render
from .models import Courses_names, Course_articles, Course_articles_modulues
from django.views.generic import DetailView


def courses_default(request):
  courses = Courses_names.objects.all
  return render(request, 'courses/courses_default.html', {'courses_names': courses})


def course_zend(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  data = {
    'courses_names': course_name,
    'course_articles': course_articles
  }
  return render(request, 'courses/course_zend.html', data)


def overall_info(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title="Общая информация")

  data = {
    'h1_title': 'Общая информация',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)


def system_requirements(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title="Системные требования")

  data = {
    'h1_title': 'Системные требования',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)


def php_example(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Пример PHP веб-сайта')
  data = {
    'h1_title': 'Пример PHP веб-сайта',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)


def security(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Безопасность')
  data = {
    'h1_title': 'Безопасность',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)

def video_course(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Видеокурс')
  data = {
    'h1_title': 'Видеокурс',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)

def patterns(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Шаблоны проектирования')
  data = {
    'h1_title': 'Паттерны(шаблоны проектирования)',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)

def main_components(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Основные компоненты')
  data = {
    'h1_title': 'Основные компоненты',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/course_zend.html', data)

def main_hrefs(request):
  course_name = Courses_names.objects.filter(title='Zend')
  course_articles = Course_articles.objects.filter(course_name__title="Zend")
  course_modules = Course_articles_modulues.objects.filter(course_article__article_title='Полезные ссылки')
  data = {
    'h1_title': 'Полезные ссылки',
    'courses_names': course_name,
    'course_articles': course_articles,
    'course_modules': course_modules
  }
  return render(request, 'courses/main_hrefs.html', data)
