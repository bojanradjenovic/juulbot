import disnake
from disnake.ext import commands
import random

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description = "Flip a coin.")
    async def coinflip(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()
        choices = ["https://www.royalmint.com/globalassets/the-royal-mint/images/pages/new-pound-coin/large_new_pound.png", "Heads"], ["https://www.royalmint.com/globalassets/the-royal-mint/images/pages/new-pound-coin/large_new_pound_rev.png", "Tails"]
        choice = random.choice(choices)
        embed = disnake.Embed(title=choice[1], color=disnake.Color.blue())
        embed.set_image(url=choice[0])
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Coinflip(bot))