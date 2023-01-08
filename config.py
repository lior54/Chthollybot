import os
from dotenv.main import load_dotenv

load_dotenv()

PREFIX="c"
BOT_NAME = "Chthollybot"
BOT_TOKEN = os.getenv("BOT_TOKEN", "")