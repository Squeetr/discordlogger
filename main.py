#MAKE SURE YOUR DISCORD BOT HAS "MESSAGE CONTENT INTENT" TURNED **ON** (Can be found in the bot tab on the discord dev portal)

token = 'YOUR DISCORD BOT TOKEN HERE'

import discord
from discord.ext import commands
import os

if not os.path.exists('log.txt'):
  open('log.txt', 'w+').close()

intents = discord.Intents().all()
bot = commands.Bot('.', intents=intents)

@bot.event
async def on_message(message):
  print("{} in {}: {}".format(str(message.author), message.guild.name, message.content))
  file = open('log.txt', 'a')
  file.write("{} in {}: {}\n".format(str(message.author), message.guild.name, message.content))
  file.close()


bot.run(token)
