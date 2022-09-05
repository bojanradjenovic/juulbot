import os
import discord
import logging
from discord.ext import commands
from datetime import datetime
date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
logger = logging.getLogger('discord')
handler = logging.FileHandler(filename=f'./logs/discord_{date}.log', encoding='utf-8', mode='a+')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
loggercommands = logging.getLogger('discord.ext')
handlercommands = logging.FileHandler(filename=f'./logs/commands_{date}.log', encoding='utf-8', mode='a+')
handlercommands.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
loggercommands.addHandler(handlercommands)
logging.basicConfig(level=logging.INFO)
bot = discord.Client()
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with a juul"), status=discord.Status.do_not_disturb)
    logger.info("Bot is ready!")

bot.load_extension("commands.avatar")
bot.load_extension("commands.profile")
bot.load_extension("commands.currency")
bot.load_extension("commands.urban")
bot.load_extension("commands.ping")
bot.load_extension("commands.cat")
bot.load_extension("commands.dog")
bot.load_extension("commands.capybara")
bot.run(os.environ["JUULBOT_TOKEN"])