import requests
import time
import os
import anthropic # using vertex api
from anthropic import AnthropicVertex
#from settings import *

from google import genai # new unified SDK
from google.genai import types

# Use this if using GCP - Vertex
from google.oauth2 import service_account

REGION = 'us-central1'
REGION_ANTHROPIC = 'us-east5'
PROJECT_ID = 'mg-ce-demos'

class Gemini2Writer:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        self.minimum_time_between_writes = 31
        self.last_write_time = 0
        self.config = types.GenerateContentConfig(
            temperature = 1.6,
            top_p = 0.98,
            max_output_tokens = 8192,
            response_modalities = ["TEXT"],
            response_mime_type="application/json",
            system_instruction = system_context,
            safety_settings = [types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
            )]
        )
        credentials = service_account.Credentials.from_service_account_file(
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.model = genai.Client(vertexai=True, project=PROJECT_ID, location=REGION, credentials=credentials)

    def write(self, prompt):
        while True:
            if time.time() - self.last_write_time >= self.minimum_time_between_writes:  
                content = [
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_text(prompt)
                        ]
                    ),
                ]
                response = self.model.models.generate_content(
                    model="gemini-2.0-flash-exp", 
                    contents=content,
                    config=self.config
                )
                self.last_write_time = time.time()
                return response.text
            else:
                time.sleep(1)

class Gemini15ProWriter:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        self.minimum_time_between_writes = 31
        self.last_write_time = 0
        self.config = types.GenerateContentConfig(
            temperature = 1.6,
            top_p = 0.98,
            max_output_tokens = 8192,
            response_modalities = ["TEXT"],
            response_mime_type="application/json",
            system_instruction = system_context,
            safety_settings = [types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
            ),types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
            )]
        )
        credentials = service_account.Credentials.from_service_account_file(
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.model = genai.Client(vertexai=True, project=PROJECT_ID, location=REGION, credentials=credentials)

    def write(self, prompt):
        while True:
            if time.time() - self.last_write_time >= self.minimum_time_between_writes:  
                content = [
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_text(prompt)
                        ]
                    ),
                ]
                response = self.model.models.generate_content(
                    model="gemini-1.5-pro", 
                    contents=content,
                    config=self.config
                )
                self.last_write_time = time.time()
                return response.text
            else:
                time.sleep(1)

class AnthropicWriterOpus:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        # Anthropic Vertex Client
        self.client = AnthropicVertex(region=REGION_ANTHROPIC, project_id=PROJECT_ID)
        self.system_context = system_context

    def write(self, prompt):
        response = self.client.messages.create(
            model="claude-3-opus",
            max_tokens=4000,
            temperature=0.8,
            system = self.system_context,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

class AnthropicWriter35Sonnet:
    def __init__(
        self,
        system_context="You are an automated assistant. Your top goal is to answer questions to the best of your ability"
    ):
        # Anthropic Vertex Client
        self.client = AnthropicVertex(region=REGION_ANTHROPIC, project_id=PROJECT_ID)
        self.system_context = system_context

    def write(self, prompt):
        response = self.client.messages.create(
            model="claude-3-5-sonnet-v2@20241022",
            max_tokens=4000,
            temperature=0.5,
            system = self.system_context,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
