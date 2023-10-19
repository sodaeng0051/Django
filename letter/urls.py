from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.letter_log, name='letter_main2'),
  path('write/', views.letter_write, name='letter_write'),
  path('list/', views.letter_list, name='letter_list'),
  ]