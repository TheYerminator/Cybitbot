from pydoc import describe
import discord
import random
from discord.ext import commands
import datetime

client = discord.Client()
client = commands.Bot(command_prefix="$$$", description="This is a Helper Bot")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_ready():
    await discord.change_presence(activity=discord.CustomActivity("Running"))
    print(discord.CustomActivity)

"""@client.event
async def help():
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)"""
    
@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    if message.author == client.user:
        return
    #Dis Hello si Hello est dis !
    if message.content.startswith('Hello'):
        embed = discord.Embed(title="Hello !", color=0x00ff00)
        await message.channel.send(embed=embed)
    #Dis Bye si Bye est dis !
    if message.content.startswith('Bye'):
        embed = discord.Embed(title="Bye !", color=0x00ff00)
        await message.channel.send(embed=embed)
    #Donne les commandes disponibles dans un embed 'Help'
    if message.content.startswith('Help'):
        embed = discord.Embed(title="Help", description = "Liste des commandes :", color=1146986)
        embed.add_field(name="Ping", value= "\U0001F3D3 Pong !", inline=False)
        embed.add_field(name="Help", value="Donne la liste des commandes", inline=False)
        embed.add_field(name="Say", value="Dis une phrase formulee par l'utilisateur votre place", inline=False)
        embed.add_field(name="Random", value="Donne une valeur aleatoire entre 0 et 1000000000", inline=False)
        embed.add_field(name="New command", value="Disponible prochainement", inline=False)
        await message.channel.send(embed=embed)
        await message.delete()
    #Réponds Pong à Ping
    if message.content.startswith('Ping'):
        embed = discord.Embed(title="\U0001F3D3 Pong !", color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.delete()
    #Donne un nombre Random
    if message.content.startswith('Random'):
        response = f'Votre nombre aleatoire est : **{random.randrange(1000000000)}**'
        await message.channel.send(response)
        await message.delete()
        return
    #Réponds à Say par ce qui suit Say
    if message.content.startswith('Say'):
        response = (message.content)
        await message.channel.send(response)
        await message.delete()
        return
    #Fais un embed
    if message.content.startswith('Embed'):
        embed = discord.Embed(title="Embed", color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.delete()
    

#Token du bot (Cybit#7254)
client.run('OTg5ODY0OTM1NjY2Mzc2NzQ4.GJYwqH.I4XzXxTFVO9no8kWBCJ3ifxjUitCR3W6njwP0k')