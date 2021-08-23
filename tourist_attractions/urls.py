from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  # <slug:studylevelslug>/<slug:subjectslug>
  path("details/<statename>/<attraction>", views.details, name="details"),
  path("state/create", views.StateCreate.as_view(), name="statecreate"),
  path("attraction/create", views.AttractionCreate.as_view(), name="attractioncreate")
]