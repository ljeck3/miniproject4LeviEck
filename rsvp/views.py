'''
INF601 - Advanced Programming in Python
Assignment: Mini Project 4
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 4

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Event
from .models import Guest

def home(request):
    return render(request, "home.html")
@login_required(login_url="/members/login_user/")
def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "rsvp/index.html", context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "rsvp/detail.html", {"event": event})

def respond(request, event_id):
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
                print(message)
            else:
                guest.has_rsvped = True
                guest.save()
                message = "Thank you for RSVPing!"
                print(message)
        except Guest.DoesNotExist:
            message = "Could not find your name on the list. Please check spelling, or contact if you believe there is an error."
            print(message)
    #return HttpResponseRedirect(reverse("rsvp:results", args=(event_id,)))
    return render(request, "rsvp/results.html", {"message": message})

def results(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "rsvp/results.html", {"event": event})
