from django.shortcuts import render
from main.models import Cards

# Create your views here.


def index(request):

    cards = Cards.objects.all()

    context = {
        "Title": "Home",
        "cards": cards,
    }
    return render(request, "main/index.html", context)
