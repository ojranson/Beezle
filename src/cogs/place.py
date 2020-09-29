from __future__ import absolute_import 
from discord.ext import commands

import json

from  src.cogs.utils.spreadsheetHandler import GSpreadWrapper

wrapper = GSpreadWrapper('TestIndu', 'Überblick')

class Place(commands.Cog):
  ''' Test Documentation '''
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True, brief='Summary HelpText', description='This is the full description of the command')
  async def place(self, ctx):
    await ctx.send('place what?')

  @place.group(invoke_without_command=True)
  async def order(self, ctx):
    await ctx.send('what order to set?')

  @order.group(invoke_without_command=True)
  async def ship(self, ctx, arg1):
    await ctx.send('what ship?')

def setup(bot):
  bot.add_cog(Place(bot))