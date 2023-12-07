import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = commands.Bot(command_prefix ="!",intents=intents)
@client.event
async def on_ready():
    print(f'Now running {client.user.name}...')
    
@client.command()
async def ping(ctx):
    await ctx.send("Pong")
client.run(TOKEN)
