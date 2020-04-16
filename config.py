import os
from dotenv import load_dotenv

load_dotenv("ENV/.env")

key = os.getenv("GCLOUD_API_KEY")  # Will be provided by mentors
wit_token = os.getenv("WIT_TOKEN")
