from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog", views.blog, name="blog"),
    path("wiki/<str:pk>", views.entries, name="detail"),
    path("create/", views.create, name="create"),
    path("duplicate/", views.duplicate, name="duplicate"),
    path("edit/<str:pk>", views.edit, name="edit"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    path("404/", views.notfound, name="notfound"),
    path('empty/', views.empty, name="empty"),
    path('password/', views.password, name="password" ),
    path('post/<str:pk>', views.post, name="post" ),
    path("render/", views.renders, name="render"),


]
