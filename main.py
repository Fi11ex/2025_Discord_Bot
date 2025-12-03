import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = app_commands.Bot(command_prefix='!', intents=discord.Intents.all())



# Bot Event
# บอทพร้อมใช้งาน
@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

# แจ้งเตือนคนเข้า-ออกเซิฟเวอร์
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1137706757511200768)
    text = f"Welcome to the server, {member.mention}!"
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัว

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1137706757511200768)
    text = f"{member.mention}has left the server!"
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้

# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'สวัสดี':
        await message.channel.send("สวัสดีจ้า มีอะไรให้ช่วยไหม") # ข้อความถูกส่งกลับ

    elif mes == 'สวัสดี บอท':
        await message.channel.send("สวัสดี, " + str(message.author.name))
    
    await bot.process_commands(message)

# กำหนดคำส่งให้บอท
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

# Slash Commands
@bot.tree.command(name='Hellobot', description='Replies with Hello')
async def Hellocommand(interaction):
    await interaction.response.send_massage('')

@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name")
async def namecommand(interaction, name : str):
    await interaction.response.send_massage(f"Hello {name}")

server_on()

bot.run(os.getenv('Token'))