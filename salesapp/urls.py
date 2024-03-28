
from django.contrib import admin
from django.urls import path

from . import views
from blog import views as blogViews
from about import views as aboutViews

# tambahan url di tempatkan di bawah ini
urlpatterns = [
    path('admin/', admin.site.urls,name='administrator'),
    path('',views.index,name='index-satu'),
    path('about/',aboutViews.index,name='about-views'),
    path('blog/',blogViews.index,name='blog-views'),
]
