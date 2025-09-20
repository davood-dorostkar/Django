from django.shortcuts import render
from django.conf import settings

def main_view(request):
    print('base directory: ', settings.BASE_DIR)
    print('static root: ', settings.STATIC_URL)
    print('media url: ', settings.MEDIA_URL)
    print('media root: ', settings.MEDIA_ROOT)
    return render(request, 'main.html')
