"""
Used to bypass the github security feature with OPENAI API Key
"""

import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MONGODB_URI = os.environ.get("MONGODB_URI")
