import discord
from psd import *

client = discord.Client()

@client.event 
async def on_ready():
    print("Hello everyone. I have beeen booted into random screenshot mode.")

@client.event
async def on_message(message):
    if message.content.startswith("./pic"):
        split_msg = message.content.split(" ")
        amount = 1
        image_link = ""

        if len(split_msg) == 2:
            try:
                amount = int(split_msg[1])

            except:
                message.channel.send("Make sure your parameter is a number")

        if amount > 5: 
            amount = 5
        elif amount < 1:
            amount = 1

        print(amount)
        for i in range(amount):
            # get image link
            image_link += get_random_link() + "\n"

        # reply with  image link
        await message.channel.send(image_link)

client.run('')