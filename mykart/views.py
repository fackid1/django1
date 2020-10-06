from django.shortcuts import render


def land(request):
    return render(request, 'shop/landing.html')
