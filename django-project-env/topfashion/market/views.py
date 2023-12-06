from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'market/home.html')

def health(request):
    return render(request, 'market/health.html')

def sales(request):
    return render(request, 'market/sales.html')

def articles(request):
    return render(request, 'market/articles.html')

def lifestyle(request):
    return render(request, 'market/lifestyle.html')

def post(request):
    return render(request, 'market/post.html')

def signIn(request):
    return render(request, 'market/sign.html')