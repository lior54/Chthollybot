import sqlite3
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

async def start(client):
        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                await client.load_extension(f"modules.{folder}.cog")
        load_dotenv()
        await client.start(os.getenv("BOT_TOKEN"))

def main():
    client = commands.Bot(intents=discord.Intents.all(), command_prefix="lior", case_insensitive=True)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to discord")
    
    asyncio.run(start(client))

if __name__ == "__main__":
    main()