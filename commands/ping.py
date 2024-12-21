import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="Get the bot's latency.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()
        embed = disnake.Embed(
            title="Pong! 🏓",
            description=f"Latency: {round(self.bot.latency * 1000)}ms",
            color=disnake.Color.blue(),
        )
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))