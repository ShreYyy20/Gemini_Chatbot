from django.urls import path, include  
from django.contrib import admin
# Don't forget to import include function
# from adminsite import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),]