import discord
from discord.ext import commands

f = open("TESTOKEN", "r")
token = f.read()

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot Ready!")

bot.run(token)