import discord
from discord.ext import commands

from src.cogs.utils.spreadsheetHandler import GSpreadWrapper

wrapper = GSpreadWrapper('TestSheet', 'TestTab')

class MiningCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

def setup(bot):
  bot.add_cog(MiningCog(bot))