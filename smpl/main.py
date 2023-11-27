import discord
from discord.ext import commands
import json

with open('config.json', encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=config['prefix'], intents=intents, help_command=None)


@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name)


@bot.command()
async def hi(ctx):
    await ctx.send("hi!")


bot.run(config['TOKEN'])
