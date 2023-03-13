from django.conf import settings
import openai


def ai_call(input_text, word_count, initial_message):
    openai.api_key = settings.OPEN_AI_API_KEY
    ans = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": f"{initial_message}, give me an answer in max {word_count} words."},
                    {"role": "user", "content": input_text},
                ]
            )
    return ans