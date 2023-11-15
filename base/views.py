from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


# Create your views here.

rooms = [{'id':1, 'name': 'Learn python'},
         {'id':2, 'name': 'Design with me'},
         {'id':3, 'name': 'Front end developers'}]

def home(request):
    # return HttpResponse("Home") #WHEN ONLY VIEWS IS USED
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context ) #WHEN TEMPLATES IS USED

def room(request, pk):
    # return HttpResponse("Room")
    room = None
    room = Room.objects.get(id=pk)
    context = {'room': room}  #SUSPECT //{'rooms':rooms} // + loop in rooms.html
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()  # < forms.py
    if request.method == 'POST':
        form == RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    context = {'form':form} 
    return render(request, 'base/room_form.html', context)    

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)

    if request.method == 'POST':
        form == RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk): #refer 1

    room = Room.objects.get(id=pk) #2
    if request.method == 'POST': #3 check method
        room.delete() #action
        return redirect('home') #2nd action 
    return render(request, 'base/delete.html', {'object':room}) #1 which object