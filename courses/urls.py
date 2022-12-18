from django.urls import path
from . import views

#Отслеживание url адресов
urlpatterns = [
    path('', views.courses_default, name='home_course'),  # Отслеживание главной страницы
    path('zend', views.overall_info, name='zend_course'),  # Zend
    path('overall', views.overall_info, name='overall_info'),
    path('system_requirements', views.system_requirements, name='system_requirements'),
    path('php_example', views.php_example, name='php_example'),
    path('security', views.security, name='security'),
    path('video_course', views.video_course, name='video_course'),
    path('patterns', views.patterns, name='patterns'),
    path('main_components', views.main_components, name='main_components'),
    path('main_hrefs', views.main_hrefs, name='main_hrefs'),
]
