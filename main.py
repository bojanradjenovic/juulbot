import discord
import logging
from discord.ext import commands
logging.basicConfig(level=logging.INFO)

bot = discord.Client()
prefix = '/'
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with a juul"), status=discord.Status.do_not_disturb)
    print("Bot is ready!")

# bot.load_extension("calculate") fix this you fucking retard
bot.load_extension("commands.avatar")
bot.load_extension("commands.profile")
bot.run('MTAwNTg2NzgxOTMyMzM3MTU3MA.Gm2Xo5.5nUxktAAtIGN2OUSRcPFQ0fOKIWuByXz6kztTo')