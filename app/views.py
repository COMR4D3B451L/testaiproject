from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .forms import ChatBotForm
from .openai import ai_call, messages
import json

class index(TemplateView):
    template_name = 'pages/main/index.html'
    
    def get(self, request, *args, **kwargs):
        request.session['message_history'] = None
        return super().get(self, request, *args, **kwargs)

def post(request):
    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        if form.is_valid():
            chat_bot_form = form.save(commit=False)  
            data = form.cleaned_data
            
            input_text = data['input_text']
            word_count = data['word_count']
            initial_message = data['initial_message']
            msg = messages(request, input_text, word_count, initial_message)
            resp = ai_call(msg)
            content = resp['choices'][0]['message']['content']
            resp_dict = json.loads(str(resp['choices'][0]['message']))
            request.session['message_history'].append(resp_dict)
            chat_bot_form.answer_text = content
            chat_bot_form.save()
            
            return TemplateResponse(request, 'pages/main/components/botresponsebubble.html', {'content': content})
        else:
            return HttpResponse('Form is invalid', status=400)
    else:
        return HttpResponse(status=403)


