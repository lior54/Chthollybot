import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
def main():
    print(TOKEN)

if __name__ == "__main__":
    main()