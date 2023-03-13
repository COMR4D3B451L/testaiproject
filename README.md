# Django-OpenAI test project

Do you want to play around with OpenAI API? You can use this django project to do so. 

To generate a Django secret key for your project, follow these steps:
    Open the Python Interactive Shell by running the command "python manage.py shell" in your project's terminal. Once you're in the shell, each new line will be prefixed with ">>>".
    Import the "get_random_secret_key()" function from "django.core.management.utils" by running the command "from django.core.management.utils import get_random_secret_key".
    Use the "get_random_secret_key()" function to generate a random secret key by running the command "print(get_random_secret_key())". The secret key will be displayed on the next line.
    create a new folder called "config" in the project directory then create a new file inside of it called "config.json".
    copy the secret and API key to the config file like the following:

    
    
    {
      "SECRET_KEY": "XXXX",
      "OPEN_AI_API_KEY": "XXXX"
    }
