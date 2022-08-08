import discord
import logging
from discord.ext import commands
logger = logging.getLogger('discord.ext')
handler = logging.FileHandler(filename='commands.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(level=logging.INFO)
@commands.command()
async def avatar(ctx, *, user: discord.User = None):
    if user == None:    
        user = ctx.author
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    embed=discord.Embed(title=f"{user.name}‘s avatar!")
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = user.colour
    await ctx.send(embed=embed)
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        user = ctx.author
        embed=discord.Embed(title=f"{user.name}‘s avatar!")
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        embed.colour = user.colour
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_command(avatar)