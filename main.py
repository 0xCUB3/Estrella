from pydoc import cli
import discord
from discord.ext import commands

# Import Bot Token
from vars import *

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Estrella is ready!")
    print("------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

client.run(token)