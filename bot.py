import os
import discord
import asyncio
import random
import json

from discord.ext import tasks, commands
from dotenv import load_dotenv
from get_voucher import get_voucher

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
client = discord.Client(command_prefix='bcs!', intents=intents)


#data
list_food = {
  "Gà nướng lu": "https://shopeefood.vn/ho-chi-minh/ga-nuong-lu-viet-huong-le-van-tho?shareChannel=copy_link",
  "Vịt quay bánh mì": "Quán đầu đường Nguyễn Văn Quá",
  "Bánh tráng trộn": "url",
  "Bánh mì": "https://shopeefood.vn/ho-chi-minh/banh-mi-dong-ri",
  "Bò Bía": "url",
  "Pizza": "url",
  "Bánh Bao nướng": "https://shopeefood.vn/ho-chi-minh/ga-nuong-o-o-o-ga-nuong-nhieu-vi-nguyen-hong-dao?shareChannel=copy_link"
}

list_drink = ["Trà Sữa", "Nước Ép", "Highlands"]

leader = "<@801662918600163379>"


#handle
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('bcs! list food'):
        foods = list(list_food.keys())
        await message.channel.send(f"@everyone list food nè: {foods}.")
        
    if message.content.startswith('bcs! random food'):
        food_key = list(list_food.keys())
        food = random.choice(food_key)
        await message.channel.send(f"@everyone Đồ ăn random được hôm nay là: **{food}** ({list_food[food]}).\nĂn uống nhiệt tình đi xếp {leader} lo hết.")

    if message.content.startswith('bcs! custom list food :'):
        str = message.content
        food_custom_raw = str.split(":")[1]
        food_custom = food_custom_raw.split(",")
        rs = random.choice(food_custom)
        await message.channel.send(f"kết quả random được là: **{rs}**.\nĂn uống nhiệt tình đi xếp {leader} lo hết.")

    
    if message.content.startswith('bcs! list drink'):
        await message.channel.send(f"@everyone list drink nè: {list_drink}.\nĂn uống nhiệt tình đi xếp {leader} lo hết.")
        
    if message.content.startswith('bcs! random drink'):
        result = random.choice(list_drink)
        await message.channel.send(f"@everyone Đồ uống random được hôm nay là: {result}.\nĂn uống nhiệt tình đi xếp {leader} lo hết.")
    
    if message.content.startswith('bcs! get voucher'):
        vouchers = get_voucher()
        str = "Mã Giảm Giá ShopeeFood Tháng 12/2022 \n"
        for key, value in vouchers.items():
            str += f"**{key}** : {value}" + "\n"
        await message.channel.send(str)
        
    if message.content.startswith('bcs! set time'):
        auto_printer.start()

#auto
@tasks.loop(seconds=10)
async def auto_printer():
    message_channel = client.get_channel(1050101954140983446)
    result = random.choice(list_drink+list(list_food.keys()))
    await message_channel.send(f"@everyone Random food hôm nay là: {result}")

@auto_printer.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")


client.run(TOKEN)