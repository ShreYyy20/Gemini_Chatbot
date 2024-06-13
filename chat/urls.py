from django.urls import path
from .views import send_message, list_messages

urlpatterns = [
    path('send', send_message, name='send_message'),
    path('', list_messages, name='list_messages'),
    path('chat/send/<int:chat_id>/', send_message, name='send_message_with_id'),
    path('chat/<int:chat_id>/', list_messages, name='list_messages_with_id'),
]
