from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .forms import ChatBotForm
from .openai import ai_call

class index(TemplateView):
    template_name = 'pages/main/index.html'

def post(request):
    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        if form.is_valid():
            chat_bot_form = form.save(commit=False)  
            data = form.cleaned_data
            
            input_text = data['input_text']
            word_count = data['word_count']
            initial_message = data['initial_message']
            resp = ai_call(input_text, word_count, initial_message)
            content = resp['choices'][0]['message']['content']
            chat_bot_form.answer_text = content
            chat_bot_form.save()
            
            return TemplateResponse(request, 'pages/main/components/botresponsebubble.html', {'content': content})
        else:
            return HttpResponse('Form is invalid', status=400)
    else:
        return HttpResponse(status=403)


