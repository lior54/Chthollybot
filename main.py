import os
import nextcord
from nextcord.ext import commands
import config
import urllib
from urllib.request import urlopen

def main():
    bot = commands.Bot(intents=nextcord.Intents.all(), command_prefix=config.PREFIX, case_insensitive=True)
    bot._help_command = None
    @bot.event
    async def on_ready():
        if bot:
            print(f"{bot.user.name} has connected to discord")

    
    @bot.event
    async def on_message(message:nextcord.message.Message):
        if bot.user.id != message.author.id and not message.author.bot:
            if "hello chtholly" in message.content.lower():
                await message.channel.send(f"Hey {message.author.mention} <:love:1063551085660344501>")
            elif 'c' in message.content[0].lower():
                message.content = 'c' + message.content[1:]
                if message.content.lower().startswith("cshutdown"):
                    await bot.process_commands(message)
                else:
                    try:
                        await bot.process_commands(message)
                    except ...:
                        await message.channel.reply(f"{message.content} is missing arguments")
    
    
    @bot.command()
    @commands.is_owner()
    async def shutdown(ctx):
        print("shutdown")
        exit(0)

    #loading cogs
    current = os.getcwd()
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            bot.load_extension(f"modules.{folder}.cog")
            os.chdir(current)

    bot.run(config.BOT_TOKEN, reconnect=True)

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