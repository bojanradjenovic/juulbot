import discord 
from discord.ext import commands
import logging
import requests
logger = logging.getLogger('discord.ext')

@commands.command()
async def dog(ctx):
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    response = requests.request("GET", f"https://dog.ceo/api/breeds/image/random")
    if response.status_code != 200:
            embed=discord.Embed(title=f"Random dog!")
            embed.description = f"Unable to retrieve a dog. Please try again later."
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            embed.colour = ctx.author.colour
            await ctx.send(embed=embed)
            return

    json = response.json()
    
    embed=discord.Embed(title=f"Random dog!")
    embed.set_image(url=f"{json['message']}")
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = ctx.author.colour
    await ctx.send(embed=embed)
@dog.error
async def dog_error(ctx, error):
     embed=discord.Embed(title=f"Random dog!")
     embed.description = f"Unable to retrieve a dog. Please try again later."
     embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
     embed.colour = ctx.author.colour
     await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(dog)