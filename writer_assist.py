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

class GeminiExpWriter:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
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
        for retry in range(10):
            while True:
                try:
                    content = [
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_text(prompt)
                            ]
                        ),
                    ]
                    response = self.model.models.generate_content(
                        model="gemini-exp-1206", 
                        contents=content,
                        config=self.config
                    )
                    return response.text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break

class Gemini2ThinkingWriter:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
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
        for retry in range(10):
            while True:
                try:
                    content = [
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_text(prompt)
                            ]
                        ),
                    ]
                    response = self.model.models.generate_content(
                        model="gemini-2.0-flash-thinking-exp-1219", 
                        contents=content,
                        config=self.config
                    )
                    return response.text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break

class Gemini2Writer:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
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
        for retry in range(10):
            while True:
                try:
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
                    return response.text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break

class Gemini15ProWriter:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
        self.config = types.GenerateContentConfig(
            temperature = 1.6,
            top_p = 0.95,
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
        for retry in range(10):
            while True:
                try:
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
                    return response.text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break

class AnthropicWriterOpus:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
        # Anthropic Vertex Client
        self.client = AnthropicVertex(region=REGION_ANTHROPIC, project_id=PROJECT_ID)
        self.system_context = system_context

    def write(self, prompt):
        for retry in range(10):
            while True:
                try:
                    response = self.client.messages.create(
                        model="claude-3-opus",
                        max_tokens=4096,
                        temperature=0.8,
                        system = self.system_context,
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    return response.content[0].text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break
        

class AnthropicWriter35Sonnet:
    def __init__(
        self,
        system_context="You are a specialized AI assistant focused on creative writing and story generation. Always respond with properly formatted JSON objects according to the specified structure.  Do not ask for feedback, only respond with content."
    ):
        # Anthropic Vertex Client
        self.client = AnthropicVertex(region=REGION_ANTHROPIC, project_id=PROJECT_ID)
        self.system_context = system_context

    def write(self, prompt):
        for retry in range(10):
            while True:
                try:
                    response = self.client.messages.create(
                        model="claude-3-5-sonnet-v2@20241022",
                        max_tokens=8000,
                        temperature=0.8,
                        system = self.system_context,
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    return response.content[0].text
                except Exception as e:
                    print(f"Attempt {retry + 1} failed: {e}")
                    time.sleep(0.5 * 2 ** retry)
                break
