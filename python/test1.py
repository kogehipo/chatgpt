import os
import requests
#import pprints
from linebot.v3 import (
    WebhookHandler
)
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
 
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say 'Hello' in Japanese",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
