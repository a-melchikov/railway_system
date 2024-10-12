from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import TrainType
from .forms import TrainTypeForm


def train_type_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "type_name")
    order = request.GET.get("order", "asc")
    fields = [("type_name", "Тип поезда")]
    train_types = TrainType.objects.all()

    if query:
        train_types = train_types.filter(type_name__icontains=query)

    if order == "asc":
        train_types = train_types.order_by(sort_field)
        next_order = "desc"
    else:
        train_types = train_types.order_by(f"-{sort_field}")
        next_order = "asc"

    return render(
        request,
        "train_types/train_type_list.html",
        {
            "train_types": train_types,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
        },
    )


def train_type_create(request):
    if request.method == "POST":
        form = TrainTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("train_type_list")
    else:
        form = TrainTypeForm()

    return render(
        request,
        "train_types/train_type_form.html",
        {
            "form": form,
            "action_url": reverse("train_type_create"),
        },
    )


def train_type_update(request, pk):
    train_type = get_object_or_404(TrainType, pk=pk)
    if request.method == "POST":
        form = TrainTypeForm(request.POST, instance=train_type)
        if form.is_valid():
            form.save()
            return redirect("train_type_list")
    else:
        form = TrainTypeForm(instance=train_type)

    return render(
        request,
        "train_types/train_type_form.html",
        {
            "form": form,
            "action_url": reverse("train_type_update", kwargs={"pk": pk}),
        },
    )


def train_type_delete(request, pk):
    train_type = get_object_or_404(TrainType, pk=pk)
    if request.method == "POST":
        train_type.delete()
        return redirect("train_type_list")

    return render(
        request,
        "train_types/train_type_confirm_delete.html",
        {"train_type": train_type},
    )
