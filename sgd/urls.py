from django.urls import path
from sgd import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sgd/<name>", views.hello_there, name="hello_there"),
    path("sgd/ml/upload", views.simple_upload, name="simple_upload"),
    path("sgd/ml/review", views.movie_review, name="movie_review")
]