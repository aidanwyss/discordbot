import discord
import asyncio
import random
import youtube_dl
import os
import logging
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = 'a!')
id = client.get_guild(500898508493029386)

players = {}

#hey :)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with them balls like its fifa'))
    print ('online')
                                 
@client.event
async def on_command_error(message, error):
    await message.send(error)

@client.event
async def on_member_join(message):
    channel = client.get_channel(566212554095853582)
    await channel.send('more gay people')      

@client.event
async def on_member_remove(message):
    channel = client.get_channel(566212554095853582)
    await channel.send('later bitch')
    
@client.command()
async def test(message):
     await message.send("yo")

@client.command()
async def dm(ctx):
    await ctx.author.send('aidans experimental bot')

@client.command()
async def ping(ctx):
    await ctx.author.send(f'Pong! {round(client.latency * 100)}ms')

@client.command(aliases=['8ball'])
async def _8ball (ctx, *, question):
    responses = [ "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."] 
    await ctx.send(f' Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(url)
    player[guild.id] = player
    player.start()

@commands.has_role('Admins')
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.author.send('KILLER QUEEN」 DAISAN NO BAKUDAN「BITES ZA DUSTO」')

@client.command()
@commands.has_role('Admins') 
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_role('Admins') 
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('NjQxOTczMDk4NDg0MjAzNTYw.XcQXWQ.TRcwOveM1PnjbUo-LHFCFoQK-E8')

