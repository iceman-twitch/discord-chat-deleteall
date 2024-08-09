import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    channel = message.channel
    messages = []
    admin_id = "your_user_id"
    
    if message.author == client.user:
        return

    if message.content.startswith('$delete') and message.author.id == admin_id:
        try:
            async for message in channel.history(limit=100):
                messages.append(message)
            for msg in messages:
                time.sleep(random.uniform(0.1, 0.4))
                await msg.delete()
                print("The message has been deleted.")
        except discord.HTTPException:
            pass
            
client.run("TOKEN")
