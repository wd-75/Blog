
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path("", blog, name="blog_list"),
    path("blog/<int:id>/",blog_detail, name="blog"),


    
    path('admin/', admin.site.urls),
]
