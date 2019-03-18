from django.urls import path
from chat_room.views import *


urlpatterns = [
    path('rooms/', RoomView.as_view()),
    path('messages/', MessageView.as_view())
]
