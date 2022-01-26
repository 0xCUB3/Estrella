from pydoc import cli
import discord
from discord.ext import commands

# Import Bot Token
from vars import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    print("Estrella is ready!")
    print("------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.event
async def on_member_join(member):
    # channel = client.get_channel(welcome_channel_id)
    # await channel.send("Hello!")
    role = discord.utils.get(member.server.roles, id="930208090643628033")
    await client.add_roles(member, role)

#@client.event
#async def on_member_remove(member):
#    channel = client.get_channel(goodbye_channel_id)
#    await channel.send("Goodbye!")

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel! Please join one, then try again.")

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Successfully left the voice channel.")
    else:
        await ctx.send("I am not in a voice channel!")

client.run(token)