from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
home_page = None
# Create your views here.
def index(request):
    return render(request, "orders/index.html")
