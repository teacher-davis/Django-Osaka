from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

rooms = [{'id':1, 'name': 'Learn python'},
         {'id':2, 'name': 'Design with me'},
         {'id':3, 'name': 'Front end developers'}]

def home(request):
    # return HttpResponse("Home") #WHEN ONLY VIEWS IS USED
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context ) #WHEN TEMPLATES IS USED

def room(request, pk):
    # return HttpResponse("Room")
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room == i
    context = {'room': room}  #SUSPECT //{'rooms':rooms} // + for in loop in rooms.html
    return render(request, 'base/room.html', context)
