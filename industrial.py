import discord
from discord.ext import commands

from spreadsheetHandler import GSpreadWrapper

wrapper = GSpreadWrapper('TestIndu', 'Überblick')

class IndustrialCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def show(self, ctx):
    await ctx.send('Show what?')

  @show.group()
  async def industrial(self, ctx, arg1="all"):
      """hilfe doc"""

      #temporary
      if arg1 == "all":
        await ctx.send("please specify with department e.g cruiser or kreuzer")
      else:
        try:
          department_row, _ = wrapper.find(arg1, in_col=1)
          result = wrapper.get_range('A{}:A{}'.format(department_row + 1, department_row + 5))

          filtered_result = list(filter(None, result))

          await ctx.send(filtered_result)
        except:
          await ctx.send("department not found. please use values as is in spreadsheet for now")

  @commands.group(invoke_without_command=True)
  async def place(self, ctx):
    await ctx.send('place what?')

  @place.group(invoke_without_command=True)
  async def order(self, ctx):
    await ctx.send('what order to set?')

  @order.group(invoke_without_command=True)
  async def ship(self, ctx, arg1):
    await ctx.send('what ship?')

def setup(bot):
  bot.add_cog(IndustrialCog(bot))