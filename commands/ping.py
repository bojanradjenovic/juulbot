import discord 
from discord.ext import commands
import logging
logger = logging.getLogger('discord.ext')

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ping(self, ctx):
        logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
        embed=discord.Embed(title=f"Pong!")
        embed.description = f"{round(self.bot.latency * 1000)}ms"
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        embed.colour = ctx.author.colour
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(ping(bot))
