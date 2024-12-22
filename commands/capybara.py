import disnake
from disnake.ext import commands
import requests

class Capybara(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description = "Get a random capybara picture.")
    async def capybara(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        response = requests.get("https://api.capy.lol/v1/capybara?json=true")
        if response.status_code != 200:
            embed = disnake.Embed(
                title="Random capybara!",
                description="Unable to retrieve a capybara. Please try again later.",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
            return
        json_data = response.json()
        embed = disnake.Embed(title="Random capybara!", color=disnake.Color.blue())
        embed.set_image(url=json_data['data']['url'])
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None
        )
        await inter.send(embed=embed)
def setup(bot):
    bot.add_cog(Capybara(bot))

