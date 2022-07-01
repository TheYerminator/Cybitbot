import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Frederic'):
        await message.channel.send("merci de ne pas m'insulter!")

client.run('OTg5ODY0OTM1NjY2Mzc2NzQ4.GkM6F1.D-M_fo0FhB0F1MXm8iMclphx5XJsW7bAmTs3FE')
