from django.urls import path
from . import views

urlpatterns = [
    path("", views.route_list, name="route_list"),
    path("create/", views.route_create, name="route_create"),
    path("<int:pk>/update/", views.route_update, name="route_update"),
    path("<int:pk>/delete/", views.route_delete, name="route_delete"),
]
