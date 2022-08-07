import discord
from discord.ext import commands
@commands.command()
async def avatar(ctx, *, user: discord.User = None):
    if user == None:    
        user = ctx.author
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