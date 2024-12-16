import disnake
from disnake.ext import commands
import json

# Load the config file
with open("config.json") as config_file:
    config = json.load(config_file)

# Set intents
intents = disnake.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.InteractionBot(intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="with a juul"), status=disnake.Status.do_not_disturb)
    print(f"Logged in as {bot.user}!")

# Load extension
bot.load_extension("commands.cat")
bot.load_extension("commands.convert")
# Run the bot
bot.run(config['token'])
