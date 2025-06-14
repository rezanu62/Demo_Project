from django.db import models

class Chat(models.Model):
    user_prompt = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.id} - {self.created_at}"
    
    
