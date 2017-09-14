from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team
from .models import Player
from .models import Venue
from .models import Match
from .models import Statistics
from .models import Enquiries
from django.db.models import Q
from .forms import EnquiriesForm
#from .forms import MessagesForm
from django.db.models import Max
from django.db.models import F
import datetime


# Create your views here.

def index(request):
    Standings = Statistics.objects.order_by('-points')
    return render(request,'index.html',{'Standings':Standings})

def result(request):
    Result = Match.objects.filter(~Q(result='')).order_by('match_id')
    Statistics = Match.objects.all()
    return render(request,'result.html',{'Result':Result,'Statistics':Statistics})

def schedule(request):
    Schedule = Match.objects.order_by('-date')
    return render(request,'schedule.html',{'Schedule':Schedule})

def teams(request):
    Teams = Team.objects.all()
    return render(request,'teams.html',{'Teams':Teams})

def Standings(request):
    Statistic= Statistics.objects.all()
    return render(request,'stats.html',{'Statistics':Statistic})

def contactus(request):
    Statistic= Statistics.objects.all()
    form = EnquiriesForm()
    return render(request,'contact_us.html',{'Statistics':Statistic,'form':form})

# def forum(request):
#     Mes= Messages.objects.all()
#     return render(request,'forum.html',{'Messages':Mes})

def stats(request):
    Statistic= Statistics.objects.order_by('-points')
    #Orange = Player.objects.all().aggregate(Max('runs'))
    Orange = Player.objects.order_by('-runs')[0]
    Purple = Player.objects.order_by('-wickets')[0]
    return render(request,'stats.html',{'Statistics':Statistic,'o':Orange,'p':Purple})

def detail(request, tid):
    details = Team.objects.get(team_id=tid)
    players = Player.objects.filter(team=tid)
    venue = Venue.objects.get(team=tid)
    return render(request,'team_detail.html',{'Details':details,'Players':players,'Venue':venue})

def post_enquiry(request):
    if request.method == "POST":
        form = EnquiriesForm(request.POST)
        if form.is_valid():
            enquiry = Enquiries(subject = form.cleaned_data['subject'],
                              name = form.cleaned_data['name'],
                              email = form.cleaned_data['email'],
                              message = form.cleaned_data['message'])
            enquiry.save()
    return render(request,'contact_us.html')

# def post_messages(request):
#     if request.method == "POST":
#         form = MessagesForm(request.POST)
#         if form.is_valid():
#             message = Messages(name = form.cleaned_data['name'],
#                               email = form.cleaned_data['email'],
#                               message = form.cleaned_data['message'])
#             message.save()
#     return render(request,'/forum.html',{'form':form})
