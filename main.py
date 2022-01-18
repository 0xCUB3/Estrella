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
    channel = client.get_channel(welcome_channel_id)
    await channel.send("Hello!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(goodbye_channel_id)
    await channel.send("Goodbye!")

client.run(token)