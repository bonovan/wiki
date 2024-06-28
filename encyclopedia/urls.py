from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("rand/", views.rand, name="rand"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create")
]
