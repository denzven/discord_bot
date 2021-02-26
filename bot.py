from asyncio import events
import discord
from discord.ext import commands
import os



bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    print("the bot is ready")
    
@bot.event
async def on_member_join(member):
    print(f"{member} has joined a server")
    
@bot.event
async def on_member_leave(member):
    print(f"{member} has left a server")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"ping ---> {round(bot.latency * 1000)} ms")
   
@bot.command()
async def test(ctx):
    await ctx.send("test")
    

#bot.run(os.getenv("BOTTOKEN"))
bot.run("ODEzOTk5MjE5NDI0NjI0NjQw.YDXd2Q.wmCHUz2btIRESPvtIdW3a6Z2IC8")
