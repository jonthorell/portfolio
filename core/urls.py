from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("encyclopedia", views.encyclopedia.as_view(), name="encyclopedia"),
    path("pirate_island", views.pirate_island.as_view(), name="pirate_island"),
    path("quiz", views.quiz.as_view(), name="quiz"),
    path("retro", views.retro.as_view(), name="retro"),
    path("projects", views.projects.as_view(), name="projects"),
    path("synth", views.synth.as_view(), name="synth"),
    path("portfolio", views.portfolio.as_view(), name="portfolio"),
]