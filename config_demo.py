import os

from dotenv import load_dotenv

load_dotenv()

mode=os.getenv("OPENBIOAI_MODE","development")
print(f"OpenBioAI mode : {mode}")
