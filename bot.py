import discord
from _sqlite3 import *

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("hello"):
        await message.channel.send("hello, I am a bot")


client.run("OTg1NzgwODIzNTA2NzAyMzk2.GLAlGp.JrRSkUjIPcoerwK17YhNSI3qoqb8q1botv_bJk")
