from django.shortcuts import render
from celeryProject.celery import add
from myapp.tasks import sub

def index(request):
    print("Results : ")
    # Enqueue the task using delay()
    result1 = add.delay(10,20)
    print("Result1: ",result1)
    result2 = sub.delay(80,10)
    print("Result2: ",result2)
    return render(request, "myapp/home.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")
