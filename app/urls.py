from .import views
from django.urls import path

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post', views.post, name='post'),
    ]