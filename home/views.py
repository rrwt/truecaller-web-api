from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    if request.method == "POST":
        return HttpResponse("requestId")
    return render(request, "home.html")
