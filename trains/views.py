from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Train
from .forms import TrainForm


def train_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "name")
    order = request.GET.get("order", "asc")

    # Поля, доступные для отображения
    fields = [
        ("name", "Название"),
        ("train_type__type_name", "Тип поезда"),
        ("stations__name", "Станции"),
    ]

    # Получение всех поездов с предварительной загрузкой связанных данных
    trains = (
        Train.objects.select_related("train_type").prefetch_related("stations").all()
    )

    # Фильтрация по запросу
    if query:
        filter_conditions = (
            Q(name__icontains=query)
            | Q(train_type__type_name__icontains=query)
            | Q(stations__name__icontains=query)
        )
        trains = trains.filter(filter_conditions).distinct()

    # Сортировка
    if order == "asc":
        trains = trains.order_by(sort_field)
        next_order = "desc"
    else:
        trains = trains.order_by(f"-{sort_field}")
        next_order = "asc"

    # Поля, доступные для сортировки
    sortable_fields = ["name", "train_type__type_name", "stations__name"]

    return render(
        request,
        "trains/train_list.html",
        {
            "trains": trains,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def train_create(request):
    if request.method == "POST":
        train_form = TrainForm(request.POST)
        if train_form.is_valid():
            train_form.save()
            return redirect("train_list")
    else:
        train_form = TrainForm()

    return render(
        request,
        "trains/train_form.html",
        {
            "train_form": train_form,
            "action_url": reverse("train_create"),
        },
    )


def train_update(request, pk):
    train = get_object_or_404(Train, pk=pk)
    if request.method == "POST":
        train_form = TrainForm(request.POST, instance=train)
        if train_form.is_valid():
            train_form.save()
            return redirect("train_list")
    else:
        train_form = TrainForm(instance=train)

    return render(
        request,
        "trains/train_form.html",
        {
            "train_form": train_form,
            "action_url": reverse("train_update", kwargs={"pk": pk}),
        },
    )


def train_delete(request, pk):
    train = get_object_or_404(Train, pk=pk)
    if request.method == "POST":
        train.delete()
        return redirect("train_list")

    return render(request, "trains/train_confirm_delete.html", {"train": train})
