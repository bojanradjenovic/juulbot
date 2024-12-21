import disnake
from disnake.ext import commands
import requests

class Dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Get a random dog picture.")
    async def dog(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code != 200:
            embed = disnake.Embed(
                title="Random dog!",
                description="Unable to retrieve a dog. Please try again later.",
                color=disnake.Color.red(),
            )
            await inter.send(embed=embed)
            return
        json_data = response.json()

        embed = disnake.Embed(title="Random dog!", color=disnake.Color.blue())
        embed.set_image(url=json_data["message"])
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.send(embed=embed)
def setup(bot):
    bot.add_cog(Dog(bot))