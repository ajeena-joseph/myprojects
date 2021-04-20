from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Team


# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,"home.html",{'obj':name})

# def about(request):
#     return render(request,"about.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
def demo(request):
    obj = Place.objects.all()
    head = Team.objects.all()
    return render(request, "index.html", {'result': obj,'group':head})
