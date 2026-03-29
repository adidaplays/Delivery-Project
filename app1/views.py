from django.shortcuts import render

def landing_page(request):
    return render(request, 'app1/landing.html')
