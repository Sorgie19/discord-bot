# bot.py
import os

import datetime
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    print(f"User ID: {message.author.id}")

    if message.author.id == 702074301758832651 and len(message.embeds) > 0:
        print("Angel sent gif")

        # go through channel's history from within the hour
        one_hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)

        async for channel_message in message.channel.history(after=one_hour_ago):
            print(f"Cycling through messages... {channel_message.author.id}")

            if channel_message.author.id == 702074301758832651 and len(message.embeds) > 0:
                await message.delete()
        # await message.delete()


# can i get a variable out here?
client.run(TOKEN)
