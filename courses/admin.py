from django.contrib import admin
from .models import Courses_names, Course_article_lists
from .models import Course_articles
from .models import Course_articles_modulues

admin.site.register(Courses_names)
admin.site.register(Course_articles)
admin.site.register(Course_articles_modulues)
admin.site.register(Course_article_lists)

