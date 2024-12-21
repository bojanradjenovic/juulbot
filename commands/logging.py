import disnake
from disnake.ext import commands
import logging

# Configure the logger
logging.basicConfig(
    filename="command_logs.log",  # Log file
    level=logging.INFO,          # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LoggingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
        user = inter.author
        command_name = inter.data.name
        # Extract command parameters
        options = inter.data.options
        params = {opt.name: opt.value for opt in options} if options else {}

        # Log the command usage with parameters
        logging.info(
            f"User: {user} ({user.id}) ran the command: /{command_name} "
            f"with parameters: {params} in guild: {inter.guild.name} ({inter.guild.id})"
        )

    @commands.Cog.listener()
    async def on_command_error(self, inter: disnake.ApplicationCommandInteraction, error):
        user = inter.author
        command_name = inter.data.name if inter.data else "Unknown Command"
        options = inter.data.options if inter.data else []
        params = {opt.name: opt.value for opt in options} if options else {}

        # Log the error with parameters
        logging.error(
            f"Error in command: /{command_name} run by {user} ({user.id}) "
            f"with parameters: {params}. Error: {error}"
        )

def setup(bot):
    bot.add_cog(LoggingCog(bot))
