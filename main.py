import os
import time
import nextcord
from nextcord.ext import commands
import config
import urllib
from urllib.request import urlopen

def main():
    client = commands.Bot(intents=nextcord.Intents.all(), command_prefix=config.PREFIX, case_insensitive=True)
    client._help_command = None
    @client.event
    async def on_ready():
        if client:
            print(f"{client.user.name} has connected to discord")

    
    @client.event
    async def on_message(message):
        if client.user.id != message.author.id and not message.author.bot:
            if "hello chtholly" in message.content.lower():
                await message.channel.send(f"Hey {message.author.mention} <:love:1063551085660344501>")
            if 'c' in message.content[0].lower():
                message.content = 'c' + message.content[1:]
                if message.content.lower().startswith("cshutdown"):
                    await client.process_commands(message)
                else:
                    try:
                        await client.process_commands(message)
                    except ...:
                        await message.channel.reply(f"{message.content} is missing arguments")
    
    @client.command()
    @commands.is_owner()
    async def shutdown(ctx):
        print("shutdown")
        exit(0)

    #loading cogs
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")
    client.run(config.BOT_TOKEN, reconnect=True)

if __name__ == "__main__":
    #waiting for wifi to connect
    while True:
        try:
            response = urlopen('http://www.google.com/').read()#will return error if wifi is not connected
            break
        except TypeError:
            pass
        except urllib.error.URLError:
            pass
    #time.sleep(10)
    
    main()