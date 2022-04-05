from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'chat/home.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

# def room(request):
#     return render(request, 'chat/room.html', {'room_name': room_name})
