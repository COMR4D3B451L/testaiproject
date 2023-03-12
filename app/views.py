from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ChatBotForm
from .openai import ai_call

class index(TemplateView):
    template_name = 'app/index.html'

def post(request):
    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        if form.is_valid():
            chat_bot_form = form.save(commit=False)  
            data = form.cleaned_data
            resp = ai_call(data['input_text'])
            content = resp['choices'][0]['message']['content']
            chat_bot_form.answer_text = content
            chat_bot_form.save()        
            return HttpResponse('<span class="text-teal-700">Bot:</span> ' + content + '<br>')
        else:
            return HttpResponse('Form is invalid', status=400)
    else:
        return HttpResponse(status=403)


