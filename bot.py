import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
  server = discord.utils.get(client.guilds, name=SERVER)

  print(
    f'{client.user} is connected to the following server:\n'
    f'{server.name}(id: {server.id})'
  )

  members = '\n - '.join([member.name for member in server.members])
  print(f'Server Members:\n - {members}')


client.run(TOKEN)