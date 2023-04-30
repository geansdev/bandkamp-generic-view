from django.urls import path

from . import views

urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
]
