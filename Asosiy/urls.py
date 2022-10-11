
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userapp.urls')),
    path('bolimlar/',include('asosiyapp.urls')),
    path('stats/',include('statsapp.urls')),
]
