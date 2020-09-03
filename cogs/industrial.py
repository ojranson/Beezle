import discord
from discord.ext import commands

from spreadsheetHandler import GSpreadWrapper

wrapper = GSpreadWrapper('TestSheet', 'TestTab')

class IndustrialCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


def setup(bot):
  bot.add_cog(IndustrialCog(bot))