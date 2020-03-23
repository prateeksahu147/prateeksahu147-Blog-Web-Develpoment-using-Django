from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects',views.projects, name= 'projects'),
    path('<int:blog_id>/', views.detail, name='projects'),
    ]