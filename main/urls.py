from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("test", views.test, name="test"),
    path("<series>", views.series, name="series"),
    path("<series>/<article>", views.article, name="article"),
]