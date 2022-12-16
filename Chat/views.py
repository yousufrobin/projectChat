from unicodedata import name
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from Chat.models import Room, Message

# Create your views here.
def index(request):
    return render(request, "home.html")


def checkview(request):
    room = request.POST.get("room_name")
    username = request.POST.get("username")
    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/" + room + "/?username=" + username)


def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    # room_details = Room.objects.filter(name=room)[0]
    # print(room_details.id)
    return render(
        request,
        "room.html",
        {"username": username, "room_details": room_details, "room": room},
    )


def send(request):
    message = request.POST.get("message")
    username = request.POST.get("username")
    room_id = request.POST.get("room_id")

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("The message has been saved to the database.")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
