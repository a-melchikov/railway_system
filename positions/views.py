from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse

from .forms import PositionForm
from .models import Position


def position_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "position_name")
    order = request.GET.get("order", "asc")

    fields = [("position_name", "Название должности")]

    positions = Position.objects.all()

    if query:
        filter_conditions = Q(position_name__icontains=query)
        positions = positions.filter(filter_conditions)

    if order == "asc":
        positions = positions.order_by(sort_field)
        next_order = "desc"
    else:
        positions = positions.order_by(f"-{sort_field}")
        next_order = "asc"

    sortable_fields = ["position_name"]

    return render(
        request,
        "positions/position_list.html",
        {
            "positions": positions,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def position_create(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("position_list")
    else:
        form = PositionForm()

    return render(
        request,
        "positions/position_form.html",
        {
            "form": form,
            "action_url": reverse("position_create"),
        },
    )


def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect("position_list")
    else:
        form = PositionForm(instance=position)

    return render(
        request,
        "positions/position_form.html",
        {
            "form": form,
            "action_url": reverse("position_update", kwargs={"pk": pk}),
        },
    )


def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        position.delete()
        return redirect("position_list")

    return render(
        request,
        "positions/position_confirm_delete.html",
        {"position": position},
    )
