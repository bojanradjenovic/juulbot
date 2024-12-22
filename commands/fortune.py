import disnake
from disnake.ext import commands
import requests

class Fortune(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Get a fortune cookie.")
    async def fortune(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code != 200:
            embed = disnake.Embed(
                title="Fortune cookie!",
                description="Unable to retrieve a fortune cookie. Please try again later.",
                color=disnake.Color.red(),
            )
            await inter.send(embed=embed)
            return
        json_data = response.json()
        embed = disnake.Embed(
            title="You open the fortune cookie and find...",
            description=json_data["slip"]["advice"], 
            color=disnake.Color.blue()
            )
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Fortune(bot))