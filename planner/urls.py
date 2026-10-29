
from django.urls import path
from . import views

app_name = "planner"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("modules/add/", views.add_module, name="add_module"),
    path("assignments/add/", views.add_assignment, name="add_assignment"),
    path("study-sessions/add/", views.add_study_session, name="add_study_session"),
]
