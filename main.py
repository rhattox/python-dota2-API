import os
from util.methods import get_match_details
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("STEAM_API_KEY")

if not api_key:
    print("API Key not found in environment variables.")
    exit(1)

get_match_details.main(api_key, '719845923')
