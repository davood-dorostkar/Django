from django.shortcuts import render
from django.conf import settings

def main_view(request):
    print(settings.BASE_DIR)
    return render(request, 'main.html')
