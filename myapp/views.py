from django.shortcuts import render
from celeryProject.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult

#Enqueue task using delay()
# def index(request):
#     print("Results : ")
#     # Enqueue the task using delay()
#     result1 = add.delay(10,20)
#     print("Result1: ",result1)
#     result2 = sub.delay(80,10)
#     print("Result2: ",result2)
#     return render(request, "myapp/home.html")\

# Enqueue task using apply_async()
# def index(request):
#     print("Results : ")
#     # Enqueue the task using delay()
#     result1 = add.apply_async(args=[10,20])
#     print("Result1: ",result1)
#     result2 = sub.apply_async(args=[80,10])
#     print("Result2: ",result2)
#     return render(request, "myapp/home.html")

def index(request):
    result = add.delay(10,30)
    return render(request, "myapp/home.html",{"result":result})
 
def check_result(request,task_id):
    # Reterieve the task result using task_id
    result = AsyncResult(task_id)
    # print("Ready: ",result.ready())
    # print("Successful: ",result.successful())
    # print("Failed: ",result.failed())
    return render(request,"myapp/result.html",{"result":result})


def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")
