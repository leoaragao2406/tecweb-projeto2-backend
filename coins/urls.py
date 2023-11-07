from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/coins', views.api_user_all),
]