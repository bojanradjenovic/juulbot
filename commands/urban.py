import json
import discord 
from discord.ext import commands
import logging
import requests
logger = logging.getLogger('discord.ext')
handler = logging.FileHandler(filename='commands.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(level=logging.INFO)
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
headers = {
    'x-rapidapi-key': "216be8f27dmshe53ba446f40d852p11a3a5jsn15ad195ee329",
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
@commands.command()
async def urban(ctx, *, word):
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    querystring = {"term":word}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    print(response)
    await ctx.send(response['list'][0]['definition'])



def setup(bot):
    bot.add_command(urban)