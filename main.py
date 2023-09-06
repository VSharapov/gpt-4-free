import openai
import load_env
import os
from pprint import pprint as pp

# Load environment variables from all .env files in the current directory
load_env.load()

openai.api_key = os.environ.get('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": '. '.join([
            'You are a helpful assistant',
            'You never apologize',
            'Your responses are no longer than they need to be'
            'You don\'t hesitate to say something is probable, or an opinion'
            'You cite sources when needed'
            ]) + '.'},
        {"role": "user", "content": "What is a dingus?"},
    ]
)

dir(openai)
pp(response)