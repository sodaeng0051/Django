from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.letter_main2, name='letter_main2'),
  path('write/', views.letter_write, name='letter_write'),
  path('<int:pk>/', views.letter_list, name='letter_list'),
  path('send/', views.letter_write, name='letter_send'),
  ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)