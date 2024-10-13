from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shoppapp.urls')),
    path('admin/', admin.site.urls),
    path('bokes/', include('bokes.urls')),
]