from django.shortcuts import render, redirect
from .models import Attendant

# Create your views here.


def index(request):
    return render(request, "index.html")


def attendants(request):
    attendants_list = Attendant.objects.all().order_by("-id")
    return render(request, "attendants.html", {"attendants": attendants_list})


def save_attendant(request):
    if request.method == "POST":
        data = Attendant.objects.create(
            name=request.POST["name"],
            department=request.POST["department"],
            level=request.POST["level"],
            contact=request.POST["contact"],
        )
        data.save()

    return redirect("/")
