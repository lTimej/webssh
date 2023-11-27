
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.LinuxWeb.as_view()),
    path('login',views.ConnectRemoteView.as_view()),
]