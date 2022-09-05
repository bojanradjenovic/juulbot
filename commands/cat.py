import os
import discord 
from discord.ext import commands
import logging
import requests
logger = logging.getLogger('discord.ext')

@commands.command()
async def cat(ctx):
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    response = requests.request("GET", f"https://cataas.com/cat?json=true")
    if response.status_code != 200:
            embed=discord.Embed(title=f"Random cat!")
            embed.description = f"Unable to retrieve a cat. Please try again later."
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            embed.colour = ctx.author.colour
            await ctx.send(embed=embed)
            return

    json = response.json()
    
    embed=discord.Embed(title=f"Random cat!")
    embed.set_image(url=f"https://cataas.com/{json['url']}")
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = ctx.author.colour
    await ctx.send(embed=embed)
@cat.error
async def cat_error(ctx, error):
     embed=discord.Embed(title=f"Random cat!")
     embed.description = f"Unable to retrieve a cat. Please try again later."
     embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
     embed.colour = ctx.author.colour
     await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(cat)