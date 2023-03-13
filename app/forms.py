from django import forms
from .models import ChatLog

class ChatBotForm(forms.ModelForm):
    initial_message = forms.CharField()
    word_count = forms.IntegerField()
    
    class Meta:
        model = ChatLog
        fields = ['input_text', 'word_count', 'initial_message']
