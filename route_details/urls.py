from django.urls import path
from . import views

urlpatterns = [
    path("", views.route_detail_list, name="route_detail_list"),
    path("create/", views.route_detail_create, name="route_detail_create"),
    path("<int:pk>/update/", views.route_detail_update, name="route_detail_update"),
    path("<int:pk>/delete/", views.route_detail_delete, name="route_detail_delete"),
]
