from django.urls import path
from .views import (
    train_type_list,
    train_type_create,
    train_type_update,
    train_type_delete,
)

urlpatterns = [
    path("", train_type_list, name="train_type_list"),
    path("create/", train_type_create, name="train_type_create"),
    path("update/<int:pk>/", train_type_update, name="train_type_update"),
    path("delete/<int:pk>/", train_type_delete, name="train_type_delete"),
]
