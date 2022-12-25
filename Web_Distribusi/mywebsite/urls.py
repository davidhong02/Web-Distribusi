from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ),
    path('about/', include('about.urls')),
    path('distribusimaterial/', include('distribusimaterial.urls')),
    path('listmaterial/', include('listmaterial.urls')),
    path('listgudang/', include('listgudang.urls')),
]
