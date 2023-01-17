import nextcord
from nextcord.ext import commands
import random
from datetime import datetime
class Gifs(commands.Cog, name="Gifs"):
    """Gif commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @nextcord.slash_command(name="hug", description="Hug the people you love")
    async def hug(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=True)):
        random.seed(datetime.now())
        urls = ["https://media.tenor.com/J7eGDvGeP9IAAAAC/enage-kiss-anime-hug.gif",
        "https://media.tenor.com/wUQH5CF2DJ4AAAAC/horimiya-hug-anime.gif",
        "https://media.tenor.com/H7i6GIP-YBwAAAAC/a-whisker-away-hug.gif",
        "https://media.tenor.com/l-46qEnHbvEAAAAC/chtholly-world-end.gif",
        "https://media.tenor.com/b3Qvt--s_i0AAAAC/hugs.gif",
        "https://media.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif",
        "https://media.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif"]
        sender = interaction.user.nick if interaction.user.nick else interaction.user.name
        sendTo = user.nick if user.nick else user.name
        embed = nextcord.Embed(color=nextcord.Color.from_rgb(random.randint(0,255), random.randint(0,255),random.randint(0,255)))
        embed.set_author(name=f"{sender} is hugging {sendTo}", icon_url=interaction.user.avatar.url)
        embed.set_image(url=urls[random.randint(0,len(urls)-1)])
        await interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Gifs(bot))