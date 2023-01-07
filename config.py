import os
from dotenv.main import load_dotenv

load_dotenv()

PREFIX="lior"
BOT_NAME = "LiorChan"
BOT_TOKEN = os.getenv("BOT_TOKEN", "")