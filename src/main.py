import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

#loads API key from .env file
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

#verifies API key exists
if api_key == None:
    raise RuntimeError("No API key")

#creates instance of agent
def creat_client() -> OpenAI:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    return client