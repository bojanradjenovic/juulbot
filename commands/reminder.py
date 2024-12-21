import disnake
from disnake.ext import commands
import asyncio

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Set a reminder.", guild_ids=[715665314964046842])
    async def reminder(
        self,
        inter: disnake.ApplicationCommandInteraction,
        time: float = commands.Param(description="The time to wait"),
        unit: str = commands.Param(choices=["s", "m", "h", "d"], description="The time unit"),
        reminder: str = commands.Param(description="The reminder message"),
    ):
        await inter.response.defer()
        
        # Confirmation message
        embed = disnake.Embed(
            title="Reminder Set! ⏰",
            description=f"Reminder set for {time}{unit} from now.",
            color=disnake.Color.blue(),
        )
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
        await inter.followup.send(embed=embed)

        # Convert time to seconds
        if unit == "m":
            time *= 60
        elif unit == "h":
            time *= 3600
        elif unit == "d":
            time *= 86400

        # Wait for the specified time
        await asyncio.sleep(time)

        await inter.followup.send(f"⏰ {inter.author.mention}, Reminder: ``{reminder}``")

def setup(bot):
    bot.add_cog(Reminder(bot))
