import disnake
from disnake.ext import commands
import requests

class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Get a random cat picture.")
    async def cat(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        response = requests.get("https://cataas.com/cat?json=true")
        if response.status_code != 200:
            embed = disnake.Embed(
                title="Random cat!",
                description="Unable to retrieve a cat. Please try again later.",
                color=disnake.Color.red(),
            )
            await inter.send(embed=embed)
            return

        json_data = response.json()

        embed = disnake.Embed(title="Random cat!", color=disnake.Color.blue())
        embed.set_image(url=f"https://cataas.com/cat/{json_data['_id']}")
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Cat(bot))
