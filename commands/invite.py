import disnake
from disnake.ext import commands
import json

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Invite link for the bot.")
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        with open("config.json") as config_file:
            config = json.load(config_file)
        await inter.response.defer()
        embed = disnake.Embed(
            title = "Invite me!",
            description = f"Click [here](https://discord.com/api/oauth2/authorize?client_id={config['client_id']}&permissions=0&scope=bot%20applications.commands) to invite me to your server!",
            color = disnake.Color.blue()
        )
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Invite(bot))