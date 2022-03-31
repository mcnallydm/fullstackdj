from django.http.response import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

def view_profile(request):
    #us = User.objects.get(username=whichuser)
    return render(request, "fullstack/profile.html", {
        "v_speakers" : Speaker.objects.all()
    })

def search(request):
    if request.method == "POST":
        keyword = request.POST["q"]
        results = Speaker.objects.filter(description__contains = keyword) | \
            Speaker.objects.filter(name__contains = keyword) | \
            Speaker.objects.filter(lastname__contains = keyword)
        return render(request, "fullstack/speakers.html", {
            "v_speakers" : results
        })

def index(request):
    return render(request, 'fullstack/index.html', {
        "v_speakers" : Speaker.objects.all()
    })

def schedule(request):
    return render(request, 'fullstack/schedule.html', {
        "v_schedule" : Schedule.objects.all(),
        "v_speakers" : Speaker.objects.all()
    })

def speakers(request):
    return render(request, 'fullstack/speakers.html', {
        "v_speakers" :  Speaker.objects.all()
    })


def speaker_detail(request, speaker_id):
    try:
        # Query to the database using a where clause
        speaker = Speaker.objects.get(id=speaker_id)
    except Speaker.DoesNotExist:
        raise Http404('speaker not found')
    return render(request, 'fullstack/speaker_detail.html', {
        "v_speaker": speaker,
        "v_speakers" : Speaker.objects.all()
    })


def about(request):
    return render(request, 'fullstack/about.html', {
        "v_speakers" : Speaker.objects.all()
    })


class speakerCreateView(CreateView):
    model = Speaker
    #fields = ['name', 'lastname', 'description']
    success_url = "/fullstack/speakers"
    form_class = SpeakerForm


class LoginInterfaceView(LoginView):
    template_name = 'fullstack/login.html'
    extra_content = {'today': datetime.today()}

class LogoutInterfaceView(LogoutView):
    template_name = 'fullstack/logout.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'fullstack/signup.html'
    success_url = '/fullstack'