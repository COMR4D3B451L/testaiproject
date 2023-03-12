from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ChatBotForm
from django.conf import settings
import openai, json




class index(TemplateView):
    template_name = 'app/index.html'
    
from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resp = ai_call(data['input_text'])
            content = resp['choices'][0]['message']['content']
            data['answer_text'] = content
            form.save()            
            return HttpResponse(content)
        else:
            print('form not valid')
    else:
        form = ChatBotForm()
    return HttpResponse()



def ai_call(chat_in):
    openai.api_key = settings.OPEN_AI_API_KEY
    ans = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "انت مساعد جيد، اعطني اجابة مختصرة ب 20 كلمة فقط"},
                    {"role": "user", "content": chat_in},
                ]
            )
    return ans