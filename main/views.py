from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Courses_names  # БД из приложения courses


# Create your views here.

def index(request):
  courses = Courses_names.objects.all
  data = {
    'course_list': 'Доступные курсы',
    'headers': ["Django фреймворк", "Zend(Laminas) фреймворк", "Coming soon", "Coming soon"],
    'descriptions': [
      "Джанго создан на основе языка Питон. За счёт Django вы можете намного проще и быстрее создавать как легкие, так и сложные веб сайты.",
      "Zend – это полностью свободный фреймворк, написанный на PHP и предназначенный для создания веб-приложений. Разработанный компанией Zend Technologies, он использует принципы MVC и ООП. Его отличительными особенностями является поддержка компонентов для интеграции сторонних служб, таких как YouTube. Идет в комплекте с Dojo (фреймворком на JavaScript) и его компонентами.",
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
    ],
    'values': ['some', 'Hello', '123'],
    'courses_names': courses
  }

  return render(request, 'main/index.html', data)


def about(request):
  return render(request, 'main/about.html')


def help(request):
  return render(request, 'main/help.html')
