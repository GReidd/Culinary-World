from django.urls import path, include
from personalCabinet import views

app_name = "personalcabinet"

urlpatterns = [
    path("", views.personalCabinet, name="personalcabinet"),
]
