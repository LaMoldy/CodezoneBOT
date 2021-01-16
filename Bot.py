import os

import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="/", intents = intents)

client.remove_command('load')
client.remove_command('unload')


@client.command
async def load(ctx, extension):
    client.load_extension()


@client.command
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print('Bot is online')


client.run("Nzk5NDMzMjQ2MTM4OTU3ODI0.YADgOg.AXgWlUpw-WqpHg26yBAOEDjXdqM")
