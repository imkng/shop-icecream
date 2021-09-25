from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

from Home.models import Contact
from django.contrib import messages


def index(request):
    context = {
        "variable": "Hi",
        "variable2": "Hello"
    }
    # messages.success(request, 'Your Message has been sent.')

    return render(request, 'index.html', context)
    # return HttpResponse("This is home Page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about Page")


def service(request):
    return render(request, 'service.html')
    # return HttpResponse("This is service Page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())

        contact.save()
        messages.success(request, 'Your Message has been sent.')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact Page")
