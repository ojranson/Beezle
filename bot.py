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

initial_extensions = ['industrial',
                      'mining']

bot = commands.Bot(command_prefix=get_prefix, description='A hard working bug')

# loading all extensions listed in [initial_extensions]
if __name__ == '__main__':
  for extension in initial_extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
  pp = pprint.PrettyPrinter()

  print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

  print(f'Successfully logged in and booted...!')

bot.run(TOKEN, bot=True, reconnect=True)