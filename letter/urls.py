from django.urls import path
from . import views

urlpatterns = [
  path('', views.letter_log, name='letter_main2'),
  path('write/', views.letter_write, name='letter_write'),
]