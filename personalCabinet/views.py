from django.shortcuts import render


# Create your views here.
def personalCabinet(request):
    return render(request, "personalCabinet/personal-cabinet.html")
