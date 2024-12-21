import disnake
from disnake.ext import commands
import requests
import json

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="weather", description="Get the weather of a location.")
    async def weather(self, inter: disnake.ApplicationCommandInteraction, location: str):
        with open("config.json") as config_file:
            config = json.load(config_file)
        api_key = config['openweathermap']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        await inter.response.defer()
        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] != 200:
                embed = disnake.Embed(
                    title="Error",
                    description=f"Could not retrieve weather data. Please check the city name and try again.",
                    color=disnake.Color.red()
                )
                await inter.followup.send(embed=embed)
                return


            city_name = data["name"]
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]


            embed = disnake.Embed(
                title=f"Weather in {city_name}",
                description=f"**{weather_description.capitalize()}**",
                color=disnake.Color.blue()
            )
            embed.add_field(name="Temperature", value=f"{temperature}°C", inline=True)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
            embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
            embed.set_footer(
            text=f"Requested by {inter.author}",
            icon_url=inter.author.avatar.url if inter.author.avatar else None,
        )
            await inter.followup.send(embed=embed)

        except Exception as e:
            embed = disnake.Embed(
                title="Error",
                description="There was an error while retrieving the weather data. Please try again later.",
                color=disnake.Color.red()
            )
            await inter.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(Weather(bot))