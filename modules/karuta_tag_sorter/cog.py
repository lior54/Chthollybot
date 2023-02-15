import os
import nextcord
from nextcord.ext import commands
import modules.karuta_tag_sorter.sorter

class Karuta(commands.Cog, name="Karuta"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="karuta_sorter", description="Recommending for sort based on ksheet, each series to be tagged must have at least one card tagged")
    async def karuta_sorter(self, interaction: nextcord.Interaction, link: str = nextcord.SlashOption(required=True, name="link", description="link to ksheet file"), exclude: str = nextcord.SlashOption(required=True, name="exclude", description="tags to exclude from tag suggestions saperated by ,")):
        if not link.startswith("https://") and link.endswith(".csv"):
            await interaction.response.send_message("invalid link")
        else:
            exclude = exclude.replace(" ", "")
            if "," in exclude:
                exclude = exclude.split(",")
            else:
                exclude = [].append(exclude)
            exclude.append("")
            data = modules.karuta_tag_sorter.sorter.karuta_sorter(link=link, exclude=exclude)
            with open(f"{interaction.user.id}.txt", "w", encoding="utf-8") as file:
                file.write(data)
            await interaction.response.send_message(file=nextcord.File(fp=f"{interaction.user.id}.txt"))
            os.remove(f"{interaction.user.id}.txt")

    @nextcord.slash_command(name="karuta_duplicates", description="Returning list of  duplicated cards")
    async def karuta_sorter(self, interaction: nextcord.Interaction, link: str = nextcord.SlashOption(required=True, name="link", description="link to ksheet file")):
        if not link.startswith("https://") and link.endswith(".csv"):
            await interaction.response.send_message("invalid link")
        else:
            data = modules.karuta_tag_sorter.sorter.karuta_duplicates(link=link, exclude=exclude)
            with open(f"{interaction.user.id}.txt", "w", encoding="utf-8") as file:
                file.write(data)
            await interaction.response.send_message(file=nextcord.File(fp=f"{interaction.user.id}.txt"))
            os.remove(f"{interaction.user.id}.txt")

def setup(bot: commands.Bot):
    bot.add_cog(Karuta(bot))