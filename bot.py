import os
import pprint

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

def get_prefix(bot, message):
  """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
  prefixes = ['?', '!', '.']

  # Check to see if we are outside of a guild. e.g DM's etc.
  if not message.guild:
    # Only allow ? to be used in DMs
    return '?'

  # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
  return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, description='A hard working bug')

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'src.cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'src.cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
  bot.unload_extension(f'src.cogs.{extension}')
  bot.load_extension(f'src.cogs.{extension}')
  
for filename in os.listdir('./src/cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'src.cogs.{filename[:-3]}')
    

@bot.event
async def on_ready():
  pp = pprint.PrettyPrinter()

  print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

  print(f'Successfully logged in and booted...!')

bot.run(TOKEN, bot=True, reconnect=True)