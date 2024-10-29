from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Personnel
from .forms import PersonnelForm


def personnel_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "full_name")
    order = request.GET.get("order", "asc")

    fields = [
        ("person_tax_id", "ИНН"),
        ("full_name", "ФИО"),
        ("station__name", "Станция"),
        ("position__position_name", "Должность"),
        ("crew__crew_name", "Бригада"),
    ]

    personnel = Personnel.objects.select_related("station", "position", "crew").all()

    if query:
        filter_conditions = (
            Q(full_name__icontains=query)
            | Q(person_tax_id__icontains=query)
            | Q(station__name__icontains=query)
            | Q(position__position_name__icontains=query)
            | Q(crew__crew_name__icontains=query)
        )
        personnel = personnel.filter(filter_conditions).distinct()

    if order == "asc":
        personnel = personnel.order_by(sort_field)
        next_order = "desc"
    else:
        personnel = personnel.order_by(f"-{sort_field}")
        next_order = "asc"

    sortable_fields = [
        "person_tax_id",
        "full_name",
        "station__name",
        "position__position_name",
        "crew__crew_name",
    ]

    return render(
        request,
        "personnel/personnel_list.html",
        {
            "personnel": personnel,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def personnel_create(request):
    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personnel_list")
    else:
        form = PersonnelForm()

    return render(
        request,
        "personnel/personnel_form.html",
        {
            "form": form,
            "action_url": reverse("personnel_create"),
        },
    )


def personnel_update(request, pk):
    person = get_object_or_404(Personnel, pk=pk)
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=person)
        if form.is_valid():    # Поля, доступные для сортировки

            form.save()
            return redirect("personnel_list")
    else:
        form = PersonnelForm(instance=person)

    return render(
        request,
        "personnel/personnel_form.html",
        {
            "form": form,
            "action_url": reverse("personnel_update", kwargs={"pk": pk}),
        },
    )


def personnel_delete(request, pk):
    person = get_object_or_404(Personnel, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("personnel_list")

    return render(
        request, "personnel/personnel_confirm_delete.html", {"person": person}
    )
