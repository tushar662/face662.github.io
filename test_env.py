from dotenv import load_dotenv
import os

load_dotenv()

print("Firebase key length:", len(os.getenv("FIREBASE_KEY") or "NOT FOUND"))
