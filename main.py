from dotenv import load_dotenv
import os

import langchain
import requests
import openai

load_dotenv()
openai.api_key = os.getenv("openai.api_key")
