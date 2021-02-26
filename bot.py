import discord
from discord.ext import commands
import os


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("the bot is ready")
    
@bot.command()
async def test(ctx):
    await ctx.send("Test")

bot.run(os.get.env("BOTTOKEN"))
