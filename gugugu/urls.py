from django.urls import path, include
from django.contrib.auth import views as auth_views
from allauth.account.views import LoginView, LogoutView, SignupView
from . import views

urlpatterns = [
    path('sg-talk', views.talk, name='talk'),
    path('sg-talk/chat', views.talk_room, name='talk_room'),
    path('sg-talk/register', views.talk_register, name='talk_register'),
    path('', views.index, name='index'),
    path('gu/ajax/validate-room-name', views.validate_room_name, name='validate_room_name'),
    path('<slug:name>', views.room, name='room'),
    path('gu/ajax/room/<int:pk>', views.room_ajax, name='room_ajax'),
    path('gu/ajax/room/<int:room_id>/message/<int:message_id>', views.clap_ajax, name='clap_ajax'),

    # name field is used in allauth
    path('gu/login', LoginView.as_view(template_name='gugugu/login.html'), name='account_login'),
    path('gu/signup', SignupView.as_view(template_name='gugugu/signup.html'), name='account_signup'),
    path('gu/logout', LogoutView.as_view(), name='account_logout'),

    path('', include('social_django.urls', namespace='social')),
]
