from django.conf.urls import include, url
from . import views

app_name = 'appone'


urlpatterns = [
   url(r'index', views.index, name='index'),
   url(r'html', views.index_html, name='index_html'),
   url(r'home', views.home, name='home'),
   url(r'authenticate', views.auth, name='authenticate'),
   url(r'main', views.main_block, name='main'),
   url(r'process', views.process, name='main')
]

