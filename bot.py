from asyncio import events
import discord
from discord.ext import commands
import os
import random

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
    
@bot.command(aliases = [ '8ball' , '8b' ])
async def _8ball(ctx,*,question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"question :{question} \nAnswer: {random.choice(responses)}")

#bot.run(os.getenv("BOTTOKEN"))