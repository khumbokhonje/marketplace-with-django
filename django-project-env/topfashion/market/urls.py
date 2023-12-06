from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health', views.health, name='health'),
    path('sales', views.sales, name='sales'),
    path('articles', views.articles, name='articles'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('health/post', views.post, name='post'),
    path('sign-in', views.signIn, name='sign-in'),
]