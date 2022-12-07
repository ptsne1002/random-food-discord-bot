import os
import discord
import asyncio
import random

from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

list_food = ["Gà", "Vịt quay bánh mì", "Bánh tráng trộn", "Bánh mì", "Bò Bía", "Pizza", "Bánh Bao"]
list_drink = ["Trà Sữa", "Nước Ép", "Highlands"]
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    auto_printer.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('!random food'):
        result = random.choice(list_food)
        await message.channel.send(f"@everyone Đồ ăn random được hôm nay là: {result}")

    if message.content.startswith('!list food'):
        await message.channel.send(f"@everyone list food: {list_food}")
    
    if message.content.startswith('!random drink'):
        result = random.choice(list_drink)
        await message.channel.send(f"@everyone Đồ uống random được hôm nay là: {result}")

    if message.content.startswith('!list drink'):
        await message.channel.send(f"@everyone list drink: {list_drink}")

@tasks.loop(seconds=5)
async def auto_printer():
    message_channel = client.get_channel(1050101954140983446)
    result = random.choice(list_drink+list_food)
    await message_channel.send(f"@everyone Random food hôm nay là: {result}")

@auto_printer.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")


client.run(TOKEN)