from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=100, default='New Chat')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat'  # Specify the table name as 'chat'

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"