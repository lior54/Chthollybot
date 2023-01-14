from nextcord.ext import commands
import asyncio
import random
class Random(commands.Cog, name="Random"):
    """Funny random commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx:commands.Context, max: str):
        """rolls number between 1 to specified num"""
        try:
            max = int(max)
        except ValueError:
            await ctx.send("Please enter a round number")
        else:
            if max < 1:
                await ctx.send("The max number must be larger than 0")
            else:
                await ctx.send("The rolled number is...")
                for i in range(3):
                    await ctx.send("🥁")
                    await asyncio.sleep(0.5)
                await ctx.send(f"{random.randint(1,max)}")
    
    @commands.command()
    async def choose(self, ctx: commands.Context, *args):
        """Choose random input
        syntax: liorchoose <option1> <option2> <option...>
        """
        if len(args) < 2:
            await ctx.send("Invalid usage of choose: liorchoose <option1> <option2> <option...>")
        else:
            choice = random.choice(args)
            await ctx.send(choice)

def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))