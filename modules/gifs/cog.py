import nextcord
from nextcord.ext import commands
from modules.gifs import generate_embed

class Gifs(commands.Cog, name="Gifs"):
    """Gif commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @nextcord.slash_command(name="hug", description="Hug the people you love")
    async def hug(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=True)):
        urls = ["https://media.tenor.com/J7eGDvGeP9IAAAAC/enage-kiss-anime-hug.gif",
        "https://media.tenor.com/wUQH5CF2DJ4AAAAC/horimiya-hug-anime.gif",
        "https://media.tenor.com/H7i6GIP-YBwAAAAC/a-whisker-away-hug.gif",
        "https://media.tenor.com/l-46qEnHbvEAAAAC/chtholly-world-end.gif",
        "https://media.tenor.com/b3Qvt--s_i0AAAAC/hugs.gif",
        "https://media.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif",
        "https://media.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif"]
        embed = generate_embed.create(interaction, user, urls, "hugging")
        await interaction.response.send_message(user.mention, embed=embed)

    
    @nextcord.slash_command(name="kiss", description="Kiss the one you desire")
    async def kiss(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=True)):
        urls = ["https://media.tenor.com/dn_KuOESmUYAAAAC/engage-kiss-anime-kiss.gif",
        "https://media.tenor.com/F02Ep3b2jJgAAAAC/cute-kawai.gif",
        "https://media.tenor.com/jnndDmOm5wMAAAAC/kiss.gif",
        "https://media.tenor.com/e5Ixi9vMTwkAAAAC/tomoya-aki-megumi-katou.gif",
        "https://media.tenor.com/8JdJyDd1higAAAAC/kiss-cheek.gif",
        "https://media.tenor.com/woA_lrIFFAIAAAAC/girl-anime.gif"]
        embed = generate_embed.create(interaction, user, urls, "kissing")
        await interaction.response.send_message(user.mention, embed=embed)
    

    @nextcord.slash_command(name="slap", description="Slap this bastard")
    async def slap(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=True)):
        urls = ["https://media.tenor.com/XiYuU9h44-AAAAAC/anime-slap-mad.gif",
        "https://media.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif",
        "https://media.tenor.com/5jBuDXkDsjYAAAAC/slap.gif",
        "https://media.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif",
        "https://media.tenor.com/l7EvbnU10M0AAAAC/nagatoro-slap.gif",
        "https://media.tenor.com/NSmlvb8xxQsAAAAd/genshin-impact-yae-miko.gif",
        "https://media.tenor.com/I5h-r5s0ptIAAAAd/suka-suka-world-end.gif"]
        embed = generate_embed.create(interaction, user, urls, "slapping")
        await interaction.response.send_message(user.mention, embed=embed)

    @nextcord.slash_command(name="punch", description="Someone deserves a punch")
    async def punch(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=True)):
        urls = ["https://media3.giphy.com/media/J0FJ0UNVg9c4mOM4Bw/giphy.gif?cid=790b76119a7fb640fb9915f82102b6ea8ae065404ec19df1&rid=giphy.gif&ct=g",
        "https://media3.giphy.com/media/2weG70cGJulPjuNOJN/giphy.gif?cid=790b7611b5bb1e145b8e589ff157ebabd3f29df8316050cc&rid=giphy.gif&ct=g",
        "https://media1.giphy.com/media/nzDs0NKindycOwVQ7X/giphy.gif?cid=790b761142714ba975b16e89f4a005b742f7a663e1371bae&rid=giphy.gif&ct=g",
        "https://media.tenor.com/D4D8Xj2rqzoAAAAC/anime-punch.gif",
        "https://64.media.tumblr.com/2850598977b96577f44a95c0277971ca/tumblr_mu544kbOCR1s6eseao1_r1_400.gif",
        "https://media.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif",
        "https://media.tenor.com/sB1uBi0REZEAAAAd/demon-lord-clayman.gif"]
        embed = generate_embed.create(interaction, user, urls, "punching")
        await interaction.response.send_message(user.mention, embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Gifs(bot))