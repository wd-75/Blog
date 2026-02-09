
from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", blog, name="blog_list"),
    path("blog/<int:id>/",blog_detail, name="blog"),


    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

