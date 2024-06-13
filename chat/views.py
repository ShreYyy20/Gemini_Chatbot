from django.shortcuts import redirect, render, get_object_or_404
from geminichatbot.settings import GENERATIVE_AI_KEY
from chat.models import ChatMessage, Chat
import google.generativeai as genai

def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == 'POST':
        genai.configure(api_key=GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        user_message = request.POST.get('user_message')
        bot_response = model.generate_content(user_message)

        ChatMessage.objects.create(chat=chat, user_message=user_message, bot_response=bot_response.text)

    return redirect('list_messages', chat_id=chat_id)

def format_bot_response(response):
    # Here you can process the response to format it properly
    # For simplicity, we'll just wrap code blocks in <pre> tags
    return response.replace('```', '<pre>').replace('```', '</pre>')

def list_messages(request, chat_id=None):
    if chat_id:
        chat = get_object_or_404(Chat, id=chat_id)
    else:
        chat = Chat.objects.first() or Chat.objects.create()

    messages = chat.messages.all().order_by('-id')[:4][::-1]  # Fetch only the last 3 messages
    return render(request, 'chat/chat.html', {'messages': messages, 'chat_id': chat.id})
