from django.shortcuts import redirect, render, get_object_or_404
from geminichatbot.settings import GENERATIVE_AI_KEY
from chat.models import ChatMessage, Chat
import google.generativeai as genai

from django.urls import reverse

def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == 'POST':
        genai.configure(api_key=GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        user_message = request.POST.get('user_message')
        bot_response = model.generate_content(user_message)

        if bot_response.text:
            ChatMessage.objects.create(chat=chat, user_message=user_message, bot_response=bot_response.text)
        else:
            pass

    return redirect(reverse('list_messages_with_id', kwargs={'chat_id': chat_id}))

def list_messages(request, chat_id=None):
    if chat_id:
        chat = get_object_or_404(Chat, id=chat_id)
    else:
        chat = Chat.objects.first() or Chat.objects.create()

    messages = chat.messages.all().order_by('-id')[:4][::-1]  
    return render(request, 'chat/chat.html', {'messages': messages, 'chat_id': chat.id})
