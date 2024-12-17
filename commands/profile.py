import disnake
from disnake.ext import commands


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Retrieve a user's profile information.")
    async def profile(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User = None
    ):
        # Default to the command user if no user is specified
        if user is None:
            user = inter.user

        try:
            embed = disnake.Embed(
                title=f"{user.name}‘s Profile",
                description=(
                    f"Username: **{user.name}**\n"
                    f"Display Name: **{user.display_name}**\n"
                    f"ID: **{user.id}**\n"
                    f"Account Creation Date: **{user.created_at.strftime('%Y-%m-%d %H:%M:%S')}**"
                ),
                color=disnake.Color.blue()
            )
            embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
            embed.set_footer(
                text=f"Requested by {inter.user.name}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None
            )

            await inter.send(embed=embed)
        except Exception as e:
           embed = disnake.Embed(
                title="Error",
                description=f"An error occurred while fetching profile. {str(e)}",
                color=disnake.Color.red()
            )

def setup(bot):
    bot.add_cog(Profile(bot))
