from django.urls import include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('rolling.urls')),
  path('accounts/', include('accounts.urls')),
]