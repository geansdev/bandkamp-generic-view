from django.urls import path
from songs import views as song_views

urlpatterns = [
    path("albums/<int:pk>/songs/", song_views.SongView.as_view()),
]
