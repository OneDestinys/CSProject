import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from translate import Translator
import requests

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

@client.command()
async def translate(ctx, *, text):
    translator = Translator(from_lang="de",to_lang="en-us")
    try:
        translated_text = translator.translate(text)
        await ctx.send(translated_text)
    except Exception as e:
        await ctx.send("Sorry, I can't translate that right now.")
@client.command() 
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    dog_url = data['message']
    await ctx.send(dog_url) 
client.run(TOKEN)
