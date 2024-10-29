from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("stations/", include("stations.urls")),
    path("train_types/", include("train_types.urls")),
    path("trains/", include("trains.urls")),
    path("positions/", include("positions.urls")),
    path("crew_directory/", include("crew_directory.urls")),
    path("personnel/", include("personnel.urls")),
    path("routes/", include("routes.urls")),
    path("route_details/", include("route_details.urls")),
]
