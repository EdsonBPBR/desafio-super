from django.contrib import admin
from django.urls import path, include  

name_app = 'portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_portal.urls')),  
]