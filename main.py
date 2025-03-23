import disnake
from disnake.ext import commands
import json


with open("config.json") as config_file:
    config = json.load(config_file)


intents = disnake.Intents.default()

bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name=config['game']), status=disnake.Status.do_not_disturb)
    print(f"Logged in as {bot.user}!")

bot.load_extension("commands.logging")
bot.load_extension("commands.cat")
bot.load_extension("commands.dog")
bot.load_extension("commands.convert")
bot.load_extension("commands.profile")
bot.load_extension("commands.ping")
bot.load_extension("commands.reminder")
bot.load_extension("commands.eightball")
bot.load_extension("commands.weather")
bot.load_extension("commands.avatar")
bot.load_extension("commands.invite")
bot.load_extension("commands.fortune")
bot.load_extension("commands.capybara")
bot.load_extension("commands.urban")
bot.load_extension("commands.translate")
bot.load_extension("commands.coinflip")

bot.run(config['token'])
