import sqlite3
import os
import nextcord
from nextcord.ext import commands
import asyncio
import config

def main():
    client = commands.Bot(intents=nextcord.Intents.all(), command_prefix=config.PREFIX, case_insensitive=True)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to discord")
    @client.event
    async def on_message(message):
        if client.user.id != message.author.id:
            if "hello" in message.content.lower():
                await message.channel.send(f"Hey {message.author.mention} this my first time here")
            await client.process_commands(message)
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")
    client.run(config.BOT_TOKEN, reconnect=True)

if __name__ == "__main__":
    main()