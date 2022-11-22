from django.urls import path
from . import views #from current folder, import the views

urlpatterns=[
    path("", views.index)
]