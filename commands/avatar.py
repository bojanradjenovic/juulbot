import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Get a user's avatar.")
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User = None):
        await inter.response.defer()
        user = user or inter.author
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        embed = disnake.Embed(
            title=f"{user}'s Avatar",
            color=disnake.Color.blue()
        )
        embed.set_image(url=avatar_url)
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))