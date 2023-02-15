import nextcord
import random
from datetime import datetime

def create(interaction: nextcord.Interaction, user: nextcord.Member, urls:list, command:str):
    random.seed(datetime.now())
    sender = interaction.user.nick if interaction.user.nick else interaction.user.name
    sendTo = user.nick if user.nick else user.name
    embed = nextcord.Embed(color=nextcord.Color.from_rgb(random.randint(0,255), random.randint(0,255),random.randint(0,255)))
    embed.set_author(name=f"{sender} is {command} {sendTo}", icon_url=interaction.user.avatar.url)
    embed.set_image(url=urls[random.randint(0,len(urls)-1)])
    return embed

def create(ctx, user: nextcord.Member, urls:list, command:str):
    random.seed(datetime.now())
    sender = ctx.user.nick if ctx.user.nick else ctx.user.name
    sendTo = user.nick if user.nick else user.name
    embed = nextcord.Embed(color=nextcord.Color.from_rgb(random.randint(0,255), random.randint(0,255),random.randint(0,255)))
    embed.set_author(name=f"{sender} is {command} {sendTo}", icon_url=ctx.user.avatar.url)
    embed.set_image(url=urls[random.randint(0,len(urls)-1)])
    return embed