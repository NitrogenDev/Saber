import discord
from discord.ext import commands
import json
import asyncio
import os
from discord.ext.commands import CommandNotFound

#custom imports
import AdminCommands
from AdminCommands import *
import BasicCommands
from BasicCommands import *
from Globals import client

os.chdir(r'D:\Saber (Discord Bot)')

@client.event
async def on_ready():
    Game = discord.Game('Type s!help for a list of commands')
    await client.change_presence(status=discord.Status.online, activity=Game)

@client.event
async def on_message(message):
        if message.author == client.user:
            return
        await client.process_commands(message)

####################################################################################

@client.event
async def on_reaction_add(reaction, user):
    print('Test1')
    if user != client.user:
        print('Test2')
        for x in ReactionMessagesData['Messages']:
            ReactionMessagesData['TempEmoteID'] = reaction.emoji
            print('Test')
            if reaction.message.id == int(x['MessageID']) and ReactionMessagesData['TempEmoteID'] == x['EmoteID']:
                role = discord.utils.find(lambda r: r.name == x['Role'], user.guild.roles)
                await user.add_roles(role)
                
@client.event
async def on_reaction_remove(reaction, user):
    if user != client.user:
        for x in ReactionMessagesData['Messages']:
            ReactionMessagesData['TempEmoteID'] = reaction.emoji
            if reaction.message.id == int(x['MessageID']) and ReactionMessagesData['TempEmoteID'] == x['EmoteID']:
                role = discord.utils.find(lambda r: r.name == x['Role'], user.guild.roles)
                await user.remove_roles(role)

####################################################################################

@client.event
async def on_member_join(member):
    await member.guild.get_channel(int(Data['JoinChannel'])).send('Welcome {user} to **{guild}**! Enjoy your stay!'.format(user=member.mention, guild=member.guild))


client.run(TOKEN)