from django.conf.urls import include, url
from . import views

app_name = 'appone'


urlpatterns = [
   url(r'index', views.index, name='index'),
   url(r'html', views.index_html, name='index_html'),
]

