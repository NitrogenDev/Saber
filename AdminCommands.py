import discord
from discord.ext import commands
from Globals import *
import json
import asyncio

@client.command(pass_context=True)
async def stop(ctx):
        role = discord.utils.find(lambda r: r.name == Data['AdminRole'], ctx.message.guild.roles)
        if role in ctx.message.author.roles:
            await ctx.send('Logout successful!')
            await client.logout()
        
@client.command(pass_context=True)
async def SetStaffRole(ctx):
                if '@' in ctx.message.content.strip('s!SetStaffRole '):
                    await ctx.send('Input the role name without mentioning it.')
                else:
                    if ctx.message.content.strip('s!SetStaffRole ') in str(ctx.guild.roles):
                        Data['AdminRole'] = ctx.message.content.strip('s!SetStaffRole ')
                        await UpdateConfig()
                    else:
                        print(ctx.message.content.strip('s!SetStaffRole '))
                        await ctx.send('**'+ctx.message.content.strip('s!SetStaffRole ')+'** is not a valid role!')

@client.command(pass_context=True)
async def ReactionRole(ctx, MessageId, role, EmoteID):
    msg = await ctx.message.channel.fetch_message(int(MessageId))
    if msg:
        await msg.add_reaction(emoji=EmoteID)
        feed = {}
        feed['MessageID'] = str(MessageId)
        feed['Role'] = role
        feed['EmoteID'] = EmoteID
        ReactionMessagesData['Messages'].append(feed)
        await UpdateReactionMessages()
        await ctx.message.delete()

@client.command(pass_context=True)
async def SetJoinChannel(ctx, id):
    Data['JoinChannel'] = ctx.message.content.strip('s!SetJoinChannel ')
    await UpdateConfig()
    '''else:
        await ctx.send("The specified channel doesn't exist!")'''

'''@client.command(pass_context=True)
async def ReactionRole(ctx, role):
    EmbedMessage = discord.Embed(
        title = '',
        description = 'React with :thumbsup: to get ' + role + ' (React with :thumbsdown: to remove the role)',
        colour = 0xFF5733
    )
    await ctx.send(embed=EmbedMessage)
    await ctx.message.delete()

async def AddReaction(message):
        await message.add_reaction(emoji=':thumbsup:609039149642809356')
        await message.add_reaction(emoji=':thumbsdown:609040887045160968')'''