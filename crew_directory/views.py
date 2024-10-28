from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse
from .forms import CrewDirectoryForm
from .models import CrewDirectory


def crew_list(request):
    query = request.GET.get("q")
    sort_field = request.GET.get("sort", "crew_name")
    order = request.GET.get("order", "asc")

    fields = [("crew_name", "Название бригады")]
    crews = CrewDirectory.objects.all()

    if query:
        filter_conditions = Q(crew_name__icontains=query)
        crews = crews.filter(filter_conditions)

    if order == "asc":
        crews = crews.order_by(sort_field)
        next_order = "desc"
    else:
        crews = crews.order_by(f"-{sort_field}")
        next_order = "asc"

    sortable_fields = ["crew_name"]

    return render(
        request,
        "crew_directory/crew_list.html",
        {
            "crews": crews,
            "fields": fields,
            "current_sort": sort_field,
            "current_order": order,
            "next_order": next_order,
            "sortable_fields": sortable_fields,
        },
    )


def crew_create(request):
    if request.method == "POST":
        form = CrewDirectoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crew_list")
    else:
        form = CrewDirectoryForm()

    return render(
        request,
        "crew_directory/crew_form.html",
        {
            "form": form,
            "action_url": reverse("crew_create"),
        },
    )


def crew_update(request, pk):
    crew = get_object_or_404(CrewDirectory, pk=pk)
    if request.method == "POST":
        form = CrewDirectoryForm(request.POST, instance=crew)
        if form.is_valid():
            form.save()
            return redirect("crew_list")
    else:
        form = CrewDirectoryForm(instance=crew)

    return render(
        request,
        "crew_directory/crew_form.html",
        {
            "form": form,
            "action_url": reverse("crew_update", kwargs={"pk": pk}),
        },
    )


def crew_delete(request, pk):
    crew = get_object_or_404(CrewDirectory, pk=pk)
    if request.method == "POST":
        crew.delete()
        return redirect("crew_list")

    return render(
        request,
        "crew_directory/crew_confirm_delete.html",
        {"crew": crew},
    )
