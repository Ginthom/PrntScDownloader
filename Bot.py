import discord
from psd import *

client = discord.Client()

@client.event 
async def on_ready():
    print("Hello everyone. I have beeen booted into random screenshot mode.")

@client.event
async def on_message(message):
    if message.content == ("./pic"):
        # get image link
        image_link = get_random_link()

        # reply with  image link
        await message.channel.send(image_link)

client.run('')