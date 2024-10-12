from django.urls import path
from .views import train_list, train_create, train_update, train_delete

urlpatterns = [
    path("", train_list, name="train_list"),
    path("create/", train_create, name="train_create"),
    path("update/<int:pk>/", train_update, name="train_update"),
    path("delete/<int:pk>/", train_delete, name="train_delete"),
]
