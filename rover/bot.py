import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from translate import Translator
import requests
import openai
import openai

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
intents = discord.Intents.all()
client = commands.Bot(command_prefix ="!",intents=intents)
@client.event
async def on_ready():
    print(f"Now running {client.user.name}...")

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def translate(ctx, *, parameters):
    args = parameters.split(" ")
    input = args[0]
    output = args[1]
    text = " ".join(args[2:])
    print(input + output)
    translator = Translator(from_lang=input,to_lang=output)
    translated_text = translator.translate(text)
    await ctx.send(translated_text)
    

@client.command() 
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    dog_url = data["message"]
    await ctx.send(dog_url) 

@client.command() 
async def pet(ctx, pats): 
    author = ctx.message.author
    if int(pats) <= 0:
        await ctx.send("please pet me at least once :(")
    else:
        await ctx.send(f"thank you for petting me {pats} times, you da best {author.display_name.lower()}")
    
@client.command()
async def feed(ctx): 
    await ctx.send ("mmm yummy!")

@client.command()
async def cmds(ctx):
    embed = discord.Embed(title = "Command List", description = "All the commands usable by Rover!", color = 0x4B006E)
    embed.add_field(name="!translate [input language code] [output language code] [text]", value = "Translate any text you want to any language!", inline = False)
    embed.add_field(name="!dog", value = "Send a cute dog picture 🐕", inline = False)
    embed.add_field(name="!ping", value = "Pongs", inline = False)
    embed.add_field(name="!pet [number]", value = "Pet Rover! He is very thankful", inline = False)
    embed.add_field(name="!feed", value = "Rover eats a tasty treat", inline = False)
    embed.add_field(name="!gpt [question]", value = "Rover will answer any question you have!")
    embed.add_field(name="!image [prompt]", value = "Rover will answer any question you have!")
    await ctx.send(embed=embed)

@client.command()
async def gpt(ctx, *, question):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=question,
        max_tokens=100
    )
    await ctx.send(response.choices[0].text.strip())
   
@client.command()
async def image(ctx, *, prompt):
    response = openai.Image.create(model = "dall-e-3", prompt=prompt,size="1024x1024",n=1)
    await ctx.send(response["data"][0]["url"])
client.run(TOKEN)

