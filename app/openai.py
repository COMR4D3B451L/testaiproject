from django.conf import settings
import openai


def messages(request, input_text, word_count, initial_message):
    messages=[
                {"role": "system", "content": f"{initial_message}, give me an answer in max {word_count} words."},
                {"role": "user", "content": input_text},
                ]
    if not request.session['message_history']:
        request.session['message_history'] = messages
        return messages
    else:
        messages = request.session['message_history']
        messages.append({"role": "user", "content": input_text})
        return messages

def ai_call(messages: list):
    openai.api_key = settings.OPEN_AI_API_KEY
    ans = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
    return ans