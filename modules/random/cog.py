from discord.ext import commands
import time
import random
class Ping(commands.Cog, name="Random"):
    """Funny random commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx:commands.Context, dice: str):
        """rolls number between 1 to specified num"""
        try:
            max = int(dice)
        except ValueError:
            await ctx.send("Please enter a number")
        else:
            await ctx.send("The rolled number is...")
            for i in range(3):
                await ctx.send("🥁")
                time.sleep(0.5)
            await ctx.send(f"{random.randint(1,max)}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))