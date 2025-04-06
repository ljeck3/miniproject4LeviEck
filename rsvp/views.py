from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Event
from .models import Guest


#def index(request):
#    return HttpResponse("Hello, world. You're at the rsvp index.")

def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "rsvp/index.html", context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        #Debug to see if name and email go through
        print(name, email)

        try:
            guest = Guest.objects.get(event=event, name=name, email=email)

            if guest.has_rsvped:
                message = "You have already RSVP'd for this event."
            else:
                guest.has_rsvped = True
                guest.save()
                message = "Thank you for RSVPing!"
        except Guest.DoesNotExist:
            message = "Sorry, you're not on the guest list for this event."

    return render(request, "rsvp/detail.html", {"event": event})
