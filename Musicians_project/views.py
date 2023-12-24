from django.shortcuts import render, redirect
from album.models import Album


def home(request):
    all_data = Album.objects.all()
    print(all_data)
    return render(request, 'home.html', {'data': all_data})
