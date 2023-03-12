from django.conf import settings
import openai


def ai_call(chat_in):
    openai.api_key = settings.OPEN_AI_API_KEY
    ans = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a good assistent, give me brief answers in max 50 words."},
                    {"role": "user", "content": chat_in},
                ]
            )
    return ans