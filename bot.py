import os
import discord
import asyncio
import random
import json

from discord.ext import tasks, commands
from dotenv import load_dotenv
from get_voucher import get_voucher
from datetime import datetime


load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
client = discord.Client(command_prefix='bcs!', intents=intents)


#data
with open("data.json", "r", encoding='utf-8') as f:
    data = json.loads(f.read())

list_food = data.get('list food')
list_drink = data.get('list drink')

#client id
leader = "<@801662918600163379>"
hg_id = "<@853495845239390208>"
ttoan_id = "<@886786917931302932>"
dthien_id = "<@868753788608069663>"

#message
wishes = " Năm mới 2023 đã đến kính chúc mọi người @everyone có một năm mới sức khoẻ dồi dào, công việc phát triển, chúc mọi người một năm 2023 thật thành công."

#handle
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #Food
    if message.content.startswith('bcs! list food'):
        foods = list(list_food.keys())
        await message.channel.send(f"@everyone list food nè: {foods}.")
        
    if message.content.startswith('bcs! random food'):
        food_key = list(list_food.keys())
        food = random.choice(food_key)
        await message.channel.send(f"@everyone Đồ ăn random được hôm nay là: **{food}** \n{list_food[food]} .\nĂn uống nhiệt tình đi Sếp {leader} lo hết.")

    if message.content.startswith('bcs! custom list food :'):
        str = message.content
        food_custom_raw = str.split(":")[1]
        food_custom = food_custom_raw.split(",")
        rs = random.choice(food_custom)
        await message.channel.send(f"kết quả random được là: **{rs}**.\nĂn uống nhiệt tình đi Sếp {leader} lo hết.")

    #Drink
    if message.content.startswith('bcs! list drink'):
        await message.channel.send(f"@everyone list drink nè: {list_drink}.\nĂn uống nhiệt tình đi Sếp {leader} lo hết.")
        
    if message.content.startswith('bcs! random drink'):
        drink_key = list(list_drink.keys())
        drink = random.choice(drink_key)
        await message.channel.send(f"@everyone Đồ uống random được hôm nay là: **{drink}** \n{list_drink[drink]} .\nĂn uống nhiệt tình đi Sếp {leader} lo hết.")
    
    
    if message.content.startswith('bcs! get voucher'):
        vouchers = get_voucher()
        str = "Mã Giảm Giá ShopeeFood Tháng 12/2022 \n"
        for key, value in vouchers.items():
            str += f"**{key}** : {value}" + "\n"
        await message.channel.send(str)
    
    if message.content.startswith('bcs! note'):
        await message.channel.send(f"@everyone Bot mới nghe được tin là {hg_id} và {ttoan_id} tuần này sẽ remote nên tranh thủ ăn lẹ lẹ mọi người ơi. :stuck_out_tongue_closed_eyes::stuck_out_tongue_closed_eyes::stuck_out_tongue_closed_eyes:") 
    
    if message.content.startswith('bcs! notification'):
        await message.channel.send(f"@everyone Bot mới nghe được tin mấy bé CTU {hg_id}, {ttoan_id}, {dthien_id} báo cáo luận văn thành công mỹ mãn nên sẽ đãi mọi người nguyên vườn gà ấy... :stuck_out_tongue_closed_eyes::stuck_out_tongue_closed_eyes::stuck_out_tongue_closed_eyes:")
    
    if message.content.startswith('bcs! bot') or message.content.startswith('bcs! oc'):
        await message.channel.send(f"Chửi bot, bot đấm cho không cản được đâu nha.. :rolling_eyes::rolling_eyes::rolling_eyes:")   
    
    if message.content.startswith('bcs! set time'):
        auto_printer.start()

#auto
@tasks.loop(seconds=1)
async def auto_printer():
    message_channel = client.get_channel(1050093968395862109)
    now_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_date = datetime(2023, 1, 22, 0, 00).strftime("%Y-%m-%d %H:%M:%S")
    if now_date == new_date:
        await message_channel.send(wishes)
    else:
        print(f"now_date: {now_date}")
        print(f"new_date: {new_date}")

@auto_printer.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")


client.run(TOKEN)
