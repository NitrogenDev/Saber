import discord
from discord.ext import commands
import json
import asyncio

client = commands.Bot(command_prefix = 's!')

with open('Config.json', 'r') as ConfigFile:
    Data = json.load(ConfigFile)
    ConfigFile.close()

with open('ReactionMessages.json', 'r') as ReactionMessages:
    ReactionMessagesData = json.load(ReactionMessages)
    ReactionMessages.close()

async def UpdateConfig():
    with open('Config.json', 'w') as ConfigFile:
        ConfigFile.write(json.dumps(Data))
        ConfigFile.close()

async def UpdateReactionMessages():
    with open('ReactionMessages.json', 'w') as ReactionMessages:
        ReactionMessages.write(json.dumps(ReactionMessagesData))
        ReactionMessages.close()