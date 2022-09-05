import discord 
from discord.ext import commands
import logging
import requests
logger = logging.getLogger('discord.ext')

@commands.command()
async def capybara(ctx):
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    response = requests.request("GET", f"https://api.capy.lol/v1/capybara?json=true")
    if response.status_code != 200:
            embed=discord.Embed(title=f"Random capybara!")
            embed.description = f"Unable to retrieve a capybara. Please try again later."
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            embed.colour = ctx.author.colour
            await ctx.send(embed=embed)
            return

    json = response.json()
    
    embed=discord.Embed(title=f"Random capybara!")
    embed.set_image(url=f"{json['data']['url']}")
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = ctx.author.colour
    await ctx.send(embed=embed)
@capybara.error
async def capybara_error(ctx, error):
     embed=discord.Embed(title=f"Random capybara!")
     embed.description = f"Unable to retrieve a capybara. Please try again later."
     embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
     embed.colour = ctx.author.colour
     await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(capybara)