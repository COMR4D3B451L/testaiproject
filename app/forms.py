from django import forms
from .models import ChatLog

class ChatBotForm(forms.ModelForm):

    class Meta:
        model = ChatLog
        fields = ['input_text']
