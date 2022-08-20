import discord
import logging
from discord.ext import commands
logger = logging.getLogger('discord')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(level=logging.INFO)

bot = discord.Client()
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with a juul"), status=discord.Status.do_not_disturb)
    print("Bot is ready!")

# bot.load_extension("calculate") fix this you fucking retard
bot.load_extension("commands.avatar")
bot.load_extension("commands.profile")
bot.load_extension("commands.currency")
bot.load_extension("commands.urban")
bot.load_extension("commands.ping")
bot.run('MTAwNTg2NzgxOTMyMzM3MTU3MA.Gm2Xo5.5nUxktAAtIGN2OUSRcPFQ0fOKIWuByXz6kztTo')