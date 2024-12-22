import disnake
from disnake.ext import commands
import requests
import json

class Urban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description = "Search for a term on Urban Dictionary.")
    async def urban(self,
        inter: disnake.ApplicationCommandInteraction,
        term: str = commands.Param(description = "The term to search for on Urban Dictionary")):
        await inter.response.defer()
        with open("config.json") as config_file:
            config = json.load(config_file)

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        headers = {
            "x-rapidapi-key": config['rapidapi'],
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        querystring = {"term": term}
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            embed = disnake.Embed(
                title="Urban Dictionary!",
                description="Unable to retrieve the term. Please try again later.",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
            return
        json_data = response.json()
        embed = disnake.Embed(
            title=f"Urban Dictionary: {term}",
            description = json_data['list'][0]['definition'],
            color=disnake.Color.blue()
        )
        embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None
        )
        await inter.send(embed=embed)
def setup(bot):
    bot.add_cog(Urban(bot))