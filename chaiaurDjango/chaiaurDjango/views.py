from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello, world! You're at chai aur Django Homepage.")



def about(request):
    return render(request, 'website/about.html')
    # return HttpResponse("Hello, world! You're at chai aur Django About page.")

def contact(request):
    return render(request, 'website/contact.html')
    # return HttpResponse("Hello, world! You're at chai aur Django Contact page.")

