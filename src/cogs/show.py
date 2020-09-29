import discord
from discord.ext import commands

import json
from src.cogs.utils.spreadsheetHandler import GSpreadWrapper

wrapper = GSpreadWrapper('TestIndu', 'Überblick')

class Show(commands.Cog):
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

  @show.group(aliases=['Frigattes', 'Frigatten', 'frigatten'])
  async def frigattes(self, ctx):
    data = self.load_from_jsonfile('res/ships/frigattes.json')
    await ctx.send(self.get_item_with_techlevel(data))

  @show.group(aliases=['Destroyer', 'Zerstörer', 'zerstörer'])
  async def destroyer(self, ctx):
    data = self.load_from_jsonfile('res/ships/destroyer.json')
    await ctx.send(self.get_item_with_techlevel(data))

  @show.group(aliases=['Cruiser', 'Kreuzer', 'kreuzer'])
  async def cruiser(self, ctx):
    data = self.load_from_jsonfile('res/ships/cruiser.json')
    await ctx.send(self.get_item_with_techlevel(data))

  @show.group()
  async def ship(self, ctx, arg1):
    with open('res/ships/cruiser.json') as json_file:
      data = json.load(json_file)
      
      results = []
      result_string = ''
      count = 0
      for ship_name, ship_info in data.items():
        count += 1
        if count == 1:
          old_value = ship_info['TechLevel']
        else:
          if old_value != ship_info['TechLevel']:
            results.append(result_string)
            old_value = ship_info['TechLevel']
            result_string = ''

          result_string += '\n{}'.format(ship_name)

          for key in ship_info:
            if ship_info[key] != None:
              result_string += '\n  {}: {}'.format(key, ship_info[key])
          result_string += '\n'

      for result in results:
        await ctx.send(result)

  def load_from_jsonfile(self, filename):
    with open(filename) as json_file:
      return json.load(json_file)

  def get_item_with_techlevel(self, data):
      result = ''
      for ship_name, ship_info in data.items():
        result += '{} {}\n'.format(ship_info['TechLevel'], ship_name)
      return result

def setup(bot):
  bot.add_cog(Show(bot))