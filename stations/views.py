from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Station
from .forms import StationForm, AddressForm


def station_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "name")
    order = request.GET.get("order", "asc")
    fields = [("name", "Название"), ("tax_id", "ИНН"), ("address", "Адрес")]
    stations = Station.objects.all()

    address_fields = ["country", "city", "street", "house", "apartment"]

    if query:
        filter_conditions = Q(name__icontains=query) | Q(tax_id__icontains=query)

        for field in address_fields:
            filter_conditions |= Q(**{f"address__{field}__icontains": query})

        stations = stations.filter(filter_conditions)

    if order == "asc":
        stations = stations.order_by(sort_field)
        next_order = "desc"
    else:
        stations = stations.order_by(f"-{sort_field}")
        next_order = "asc"

    sortable_fields = ["name", "tax_id", "address"]

    return render(
        request,
        "stations/station_list.html",
        {
            "stations": stations,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def station_create(request):
    if request.method == "POST":
        address_form = AddressForm(request.POST)
        station_form = StationForm(request.POST)
        if address_form.is_valid() and station_form.is_valid():
            address = address_form.save()
            station = station_form.save(commit=False)
            station.address = address
            station.save()
            return redirect("station_list")
    else:
        address_form = AddressForm()
        station_form = StationForm()

    return render(
        request,
        "stations/station_form.html",
        {
            "address_form": address_form,
            "station_form": station_form,
            "action_url": reverse("station_create"),
        },
    )


def station_update(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        address_form = AddressForm(request.POST, instance=station.address)
        station_form = StationForm(request.POST, instance=station)
        if address_form.is_valid() and station_form.is_valid():
            address_form.save()
            station_form.save()
            return redirect("station_list")
    else:
        address_form = AddressForm(instance=station.address)
        station_form = StationForm(instance=station)

    return render(
        request,
        "stations/station_form.html",
        {
            "address_form": address_form,
            "station_form": station_form,
            "action_url": reverse("station_update", kwargs={"pk": pk}),
        },
    )


def station_delete(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        station.delete()
        return redirect("station_list")

    return render(request, "stations/station_confirm_delete.html", {"station": station})
