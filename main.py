import discord, datetime
from discord.utils import get
import os
import random
import time
from asyncio import sleep
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from replit import db
from config import *

TOKEN = "NzE1MTk5NDAzOTU0Mjc0Mzg1.Xs5vWQ.0O4uYJe6ouMnfBBNZktdN2egzPc"

Client = discord.Client()

ball_responses = [
    "Hell nawww",
    "That's ong",
    "Just stfu and lick my tits already...",
    "Ask cutty312",
    "Yessir",
    "I'd say so",
    "I think so",
    "No doubt whatsoever",
    "no",
    "Just no...",
    "That's cap",
    "Before you ask me another question, get a fucking life outside of discord...",
    "Nahh",
    "Google it up jeeez",
    "yes and no...",
    "i dont fucking know",
    "NO no NOOO"
]

sus_responses = [
    "Sure dawg fuck me from behind",
    "Put it in me big guy",
    "Thank you daddy<3",
    "Yes daddy yessss",
    "Rail me"
]

friendly_responses = [
    "Bonjour",
    "Hello there how may I help you...",
    "What's good boys",
    "WADDUPP",
    "why",
    "no",
    "What's poppin",
    "Hello World",
    "ROCKETS IN 7"
]

client = commands.Bot(command_prefix="3")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome! We are a community that talks about the 3 big things in life --- basketball, jazz music, and computer science skills.  Enjoy your stay!')
    channel = client.get_channel(832264206849802307)
    await channel.send("Whale cum!! \n :sweat_drops: \n :whale:")


@client.event
async def on_ready():
    print("RUNNING :)")


@client.command()
async def bump(ctx):
    while True:
        channel = client.get_channel(832274490423509073)
        await channel.send("!d bump")
        time.sleep(7500)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned")


@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Menace to Society")
    await member.add_roles(role)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Menace to Society")
    await member.remove_roles(role)


@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("warn"):
        await message.channel.send("Ayo this is your last straw motherfucker.")
        return

    if "fuck you" in message.content.lower():
        await message.channel.send(random.choice(sus_responses))
        return

    if message.content.startswith("ping"):
        await message.channel.send("pong")
        return

    if message.content.startswith("!d bump"):
        await message.channel.send("Thx mate... my respect for u just went off the charts, no cap.")
        return

    if message.content.startswith("say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()
        return

    if message.content.startswith("8ball"):
        await message.channel.send(random.choice(ball_responses))
        return

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
        return

    elif message.content.startswith('hi'):
        await message.channel.send(random.choice(friendly_responses))


client.run(TOKEN)
