import os
import nextcord
from nextcord.ext import commands
import config

def main():
    client = commands.Bot(intents=nextcord.Intents.all(), command_prefix=config.PREFIX, case_insensitive=True)
    client._help_command = None
    @client.event
    async def on_ready():
        if client:
            print(f"{client.user.name} has connected to discord")

    
    @client.event
    async def on_message(message):
        if client.user.id != message.author.id:
            if "hello chtholly" in message.content.lower():
                await message.channel.send(f"Hey {message.author.mention} <:love:1063551085660344501>")
            if 'c' in message.content[0].lower():
                message.content = 'c' + message.content[1:]
            await client.process_commands(message)
    
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
    if not os.path.exists("modules"):
        os.chdir("./bot/Chthollybot")
    main()