from django.urls import include

urlpatterns = [
  path('accounts/', include('accounts.urls')),
]