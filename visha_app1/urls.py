from django.urls import path
from visha_app1 import views

urlpatterns = [
    path('', views.home_page)
]