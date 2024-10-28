from django.urls import path
from . import views

urlpatterns = [
    path("", views.crew_list, name="crew_list"),
    path("create/", views.crew_create, name="crew_create"),
    path("update/<int:pk>/", views.crew_update, name="crew_update"),
    path("delete/<int:pk>/", views.crew_delete, name="crew_delete"),
]
