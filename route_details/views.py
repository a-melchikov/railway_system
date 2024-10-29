from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RouteDetail
from .forms import RouteDetailForm


from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RouteDetail
from .forms import RouteDetailForm


def route_detail_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "route__train__name")
    order = request.GET.get("order", "asc")

    fields = [
        ("route__train__name", "Поезд"),
        ("stop_number", "Номер остановки"),
        ("stop_station__name", "Станция остановки"),
        ("arrival_time", "Время прибытия"),
        ("departure_time", "Время отправления"),
    ]

    route_details = RouteDetail.objects.select_related("route", "stop_station")

    if query:
        filter_conditions = Q(route__train__name__icontains=query) | Q(
            stop_station__name__icontains=query
        )
        route_details = route_details.filter(filter_conditions).distinct()

    if order == "desc":
        sort_field = f"-{sort_field}"
    route_details = route_details.order_by(sort_field)

    current_sort = request.GET.get("sort", "route__train__name")
    current_order = order
    next_order = "desc" if order == "asc" else "asc"

    return render(
        request,
        "route_details/route_detail_list.html",
        {
            "route_details": route_details,
            "fields": fields,
            "current_sort": current_sort,
            "current_order": current_order,
            "next_order": next_order,
        },
    )


def route_detail_create(request):
    if request.method == "POST":
        form = RouteDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("route_detail_list")
    else:
        form = RouteDetailForm()

    return render(
        request,
        "route_details/route_detail_form.html",
        {
            "form": form,
            "action_url": reverse("route_detail_create"),
        },
    )


def route_detail_update(request, pk):
    route_detail = get_object_or_404(RouteDetail, pk=pk)
    if request.method == "POST":
        form = RouteDetailForm(request.POST, instance=route_detail)
        if form.is_valid():
            form.save()
            return redirect("route_detail_list")
    else:
        form = RouteDetailForm(instance=route_detail)

    return render(
        request,
        "route_details/route_detail_form.html",
        {
            "form": form,
            "action_url": reverse("route_detail_update", kwargs={"pk": pk}),
        },
    )


def route_detail_delete(request, pk):
    route_detail = get_object_or_404(RouteDetail, pk=pk)
    if request.method == "POST":
        route_detail.delete()
        return redirect("route_detail_list")

    return render(
        request,
        "route_details/route_detail_confirm_delete.html",
        {"route_detail": route_detail},
    )
