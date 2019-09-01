from django.shortcuts import render
from django.contrib import messages

from home.api import fetch_request_id, fetch_user_information


def home_page(request):
    context = {}
    if request.method == "POST":
        status_code, request_id = fetch_request_id(request.POST.get("phone_number"))

        if status_code == 200:
            context = fetch_user_information(request_id)

            if context['status'] != 200:
                messages.error(request, context['message'])
        else:
            messages.error(request, request_id)

    return render(request, "home.html", context=context)
