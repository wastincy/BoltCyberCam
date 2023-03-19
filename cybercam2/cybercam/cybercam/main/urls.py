from django.urls import path
from . import views

urlpatterns = [
    path('', views.singin),
    path('/singin', views.singin),
    path('postsing', views.postsing),
]
