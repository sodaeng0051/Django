from django.urls import path
from . import views

urlpatterns = [
  path('', views.letter_log, name='letter_log')
]