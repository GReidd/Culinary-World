from django.shortcuts import render
from main.models import Cards


# Create your views here.
def recipes(request):
    cards = Cards.objects.all()

    context = {
        "Title": "Recipes",
        "cards": cards,
    }

    return render(request, "goods/recipes.html", context)


def recipePage(request):
    return render(request, "goods/recipe-page.html")
