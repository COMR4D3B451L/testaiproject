from django.db import models

class ChatLog(models.Model):
    input_text = models.CharField(max_length=8192)
    answer_text = models.CharField(max_length=8192)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input_text} - {self.answer_text}"
