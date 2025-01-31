from datetime import datetime
from abc import ABC
import time
import logging
from openai import OpenAI
from transformers import pipeline
from huggingface_hub import login
import requests
from config import MISTRAL_API_KEY, OPENAI_API_KEY


class LlmHandler(ABC):
    def __init__(self):
        return None

class MistralHandler(LlmHandler):
    def __init__(self):
        self.sleeptime = 1
        self.max_tokens = 512
        self.temperature = 0.5
        self.top_p = 0.5
        self.url = "https://api.mistral.ai/v1/chat/completions"
        self.model = "mistral-tiny"

        self.payload = ''
        self.headers = ''

        return None

    def call(self, system_content, prompt):
        self.headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        self.payload = {
            "model": self.model, 
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p
        }

        time.sleep(self.sleeptime)

        response = requests.post(self.url, json=self.payload, headers=self.headers)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Fehler: {response.status_code}, {response.text}"


class Gpt4oHandler(LlmHandler):
    def __init__(self):
        self.sleeptime = 0.1
        self.temperature = 0.5
        self.top_p = 0.5
        self.model = "gpt-4o-mini"


    def call(self, system_content, prompt):
        client = OpenAI(api_key = OPENAI_API_KEY)

        dialogue = client.chat.completions.create(
           model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature, 
            top_p=self.top_p
        )

        time.sleep(self.sleeptime)
        return dialogue.choices[0].message.content
