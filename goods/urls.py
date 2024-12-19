from django.urls import path, include
from goods import views

app_name = "goods"

urlpatterns = [
    path("", views.recipes, name="recipes"),
    path("recipepage/", views.recipePage, name="recipe-page"),
]
