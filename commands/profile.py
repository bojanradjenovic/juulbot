import discord
from discord.ext import commands
import logging
logger = logging.getLogger('discord.ext')
@commands.command()
async def profile(ctx, *, user: discord.User = None):
    if user == None:    
        user = ctx.author
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    embed=discord.Embed(title=f"{user.name}‘s profile!")
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Username" ,value=f"{user.name}#{user.discriminator}", inline=False)
    embed.add_field(name="Display name" ,value=f"{user.display_name}", inline=False)
    embed.add_field(name="ID" ,value=f"{user.id}", inline=False)
    embed.add_field(name="Account creation date" ,value=f"{user.created_at}", inline=False)
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = user.colour
    await ctx.send(embed=embed)

@profile.error
async def profile_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        user = ctx.author
        embed=discord.Embed(title=f"{user.name}‘s profile!")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Username" ,value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="Display name" ,value=f"{user.display_name}", inline=False)
        embed.add_field(name="ID" ,value=f"{user.id}", inline=False)
        embed.add_field(name="Account creation date" ,value=f"{user.created_at}", inline=False)
        embed.set_footer(text="{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        embed.colour = user.colour
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_command(profile)