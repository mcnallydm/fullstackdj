from django.urls import path
from . import views


urlpatterns = [
    path ("", views.index, name="index"),
    path ("schedule", views.schedule, name="schedule"),
    path ("speakers", views.speakers, name="speakers"),
    path ("speaker/<int:speaker_id>/", views.speaker_detail, name="speaker_detail"),
    path ("about", views.about, name="about"),
    path ("speakers/new", views.speakerCreateView.as_view(), name="new_speaker"),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("search", views.search, name="search"),
]
