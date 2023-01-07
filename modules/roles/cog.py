from nextcord.ext import commands

class Roles(commands.Cog, name="Roles"):
    """Create button roles"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roles(self, ctx:commands.Context):
        """Check for a response from the bot"""
        await ctx.send("in development")

def setup(bot: commands.Bot):
    bot.add_cog(Roles(bot))