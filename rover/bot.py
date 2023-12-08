import os
import discord
<<<<<<< HEAD
from dotenv import load_dotenv
=======
from translate import Translator
import requests
>>>>>>> 3f09db3344c20db71ea4e02df82264ac021c1f78

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
client = discord.Client(intents=intents)
print(TOKEN)
@client.event
async def on_ready():
<<<<<<< HEAD
    print(f'{client.user} has connected to Discord!')

=======
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
>>>>>>> 3f09db3344c20db71ea4e02df82264ac021c1f78
client.run(TOKEN)


