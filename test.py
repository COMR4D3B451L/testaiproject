import openai_secret_manager

# get the api key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# set the api key
import openai
openai.api_key = secrets["api_key"]
