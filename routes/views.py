from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Route
from .forms import RouteForm


def route_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "train__name")
    order = request.GET.get("order", "asc")

    fields = [
        ("owner_station__name", "Станция-владелец"),
        ("train__name", "Поезд"),
        ("departure_station__name", "Станция отправления"),
        ("arrival_station__name", "Станция прибытия"),
        ("departure_time", "Время отправления"),
        ("arrival_time", "Время прибытия"),
        ("crew__crew_name", "Бригада"),
    ]

    routes = Route.objects.select_related(
        "owner_station", "train", "departure_station", "arrival_station", "crew"
    )

    if query:
        filter_conditions = (
            Q(owner_station__name__icontains=query)
            | Q(train__name__icontains=query)
            | Q(departure_station__name__icontains=query)
            | Q(arrival_station__name__icontains=query)
            | Q(crew__crew_name__icontains=query)
        )
        routes = routes.filter(filter_conditions).distinct()

    if order == "asc":
        routes = routes.order_by(sort_field)
        next_order = "desc"
    else:
        routes = routes.order_by(f"-{sort_field}")
        next_order = "asc"

    sortable_fields = [
        "owner_station__name",
        "train__name",
        "departure_station__name",
        "arrival_station__name",
        "departure_time",
        "arrival_time",
        "crew__name",
    ]

    return render(
        request,
        "routes/route_list.html",
        {
            "routes": routes,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def route_create(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("route_list")
    else:
        form = RouteForm()

    return render(
        request,
        "routes/route_form.html",
        {
            "form": form,
            "action_url": reverse("route_create"),
        },
    )


def route_update(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect("route_list")
    else:
        form = RouteForm(instance=route)

    return render(
        request,
        "routes/route_form.html",
        {
            "form": form,
            "action_url": reverse("route_update", kwargs={"pk": pk}),
        },
    )


def route_delete(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        route.delete()
        return redirect("route_list")

    return render(request, "routes/route_confirm_delete.html", {"route": route})
