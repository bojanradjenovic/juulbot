import disnake
from disnake.ext import commands
import requests
from decimal import Decimal, ROUND_HALF_UP
import pint
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

class Convert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Perform various conversions.")
    async def convert(self, inter: disnake.ApplicationCommandInteraction):
        pass 


    @convert.sub_command(description="Convert between currencies.")
    async def currency(
        self,
        inter: disnake.ApplicationCommandInteraction,
        from_currency: str = commands.Param(choices=["EUR", "USD", "GBP", "CAD", "DKK", "AED", "MAD", "BGN", "RSD", "INR", "IDR", "MYR", "CHF", "CNY", "JPY", "TRY", "RUB", "EGP", "PHP"], description="The currency to convert from"),
        to_currency: str = commands.Param(choices=["EUR", "USD", "GBP", "CAD", "DKK", "AED", "MAD", "BGN", "RSD", "INR", "IDR", "MYR", "CHF", "CNY", "JPY", "TRY", "RUB", "EGP", "PHP"], description="The currency to convert to"),
        amount: float = commands.Param(description="Amount to convert"),
    ):
        await inter.response.defer()
        
        cents = Decimal('0.01')
        rounded_amount = Decimal(amount).quantize(cents, ROUND_HALF_UP)

        api_url = (
            f"https://www.mastercard.co.uk/settlement/currencyrate/conversion-rate"
            f"?fxDate=0000-00-00&transCurr={from_currency}&crdhldBillCurr={to_currency}&bankFee=0&transAmt={rounded_amount}"
        )
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"
        }
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()

            data = response.json()
            conversion_rate = data.get("data", {}).get("conversionRate")
            converted_amount = data.get("data", {}).get("crdhldBillAmt")
            fx_date = data.get("data", {}).get("fxDate")
            if conversion_rate is None or converted_amount is None:
                raise ValueError("Missing data in API response")

            embed = disnake.Embed(
                title="Currency Conversion",
                description=(
                    f"**{amount} {from_currency}** ➡ **{Decimal(converted_amount):.2f} {to_currency}**\n"
                    f"Conversion Rate: **{Decimal(conversion_rate):.6f}**\n"
                    f"Rate Date: {fx_date}"
                ),
                color=disnake.Color.blue()
            )
            embed.set_footer(
                text=f"Requested by {inter.user}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None,
            )
            await inter.send(embed=embed)

        except Exception as e:
            embed = disnake.Embed(
                title="Error",
                description=f"An error occurred while converting currencies. {str(e)}",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
    @convert.sub_command(description="Convert between length units.")
    async def length(
        self,
        inter: disnake.ApplicationCommandInteraction,
        from_unit: str = commands.Param(choices=["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard"], description="The length unit to convert from"),
        to_unit: str = commands.Param(choices=["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard"], description="The length unit to convert to"),
        value: float = commands.Param(description="Length value to convert"),
    ):
        await inter.response.defer()
        try:
            # Perform the conversion
            quantity = value * ureg(from_unit)
            converted_quantity = quantity.to(to_unit)

            embed = disnake.Embed(
                title="Length Conversion",
                description=(
                    f"**{value} {from_unit}** ➡ **{converted_quantity.magnitude:.2f} {to_unit}**"
                ),
                color=disnake.Color.blue()
            )
            embed.set_footer(
                text=f"Requested by {inter.user}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None,
            )
            await inter.send(embed=embed)

        except Exception as e:
            
            embed = disnake.Embed(
                title="Error",
                description=f"An error occurred while converting units. {str(e)}",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)

    
    @convert.sub_command(description="Convert between weight units.")
    async def weight(
        self,
        inter: disnake.ApplicationCommandInteraction,
        from_unit: str = commands.Param(choices=["kilogram", "gram", "pound", "ounce"], description="The weight unit to convert from"),
        to_unit: str = commands.Param(choices=["kilogram", "gram", "pound", "ounce"], description="The weight unit to convert to"),
        value: float = commands.Param(description="Weight value to convert"),
    ):
        await inter.response.defer()
        try:
            # Perform the conversion 
            quantity = value * ureg(from_unit)
            converted_quantity = quantity.to(to_unit)

            embed = disnake.Embed(
                title="Weight Conversion",
                description=(
                    f"**{value} {from_unit}** ➡ **{converted_quantity.magnitude:.2f} {to_unit}**"
                ),
                color=disnake.Color.blue()
            )
            embed.set_footer(
                text=f"Requested by {inter.user}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None,
            )
            await inter.send(embed=embed)

        except Exception as e:
            
            embed = disnake.Embed(
                title="Error",
                description=f"An error occurred while converting units. {str(e)}",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
    @convert.sub_command(description="Convert between temperature units.")
    async def temperature(
        self,
        inter: disnake.ApplicationCommandInteraction,
        from_unit: str = commands.Param(choices=["celsius", "fahrenheit", "kelvin"], description="The temperature unit to convert from"),
        to_unit: str = commands.Param(choices=["celsius", "fahrenheit", "kelvin"], description="The temperature unit to convert to"),
        value: float = commands.Param(description="Temperature value to convert"),
):
        await inter.response.defer()
        try:
            # Perform the conversion
            quantity = Q_(value, ureg(from_unit))
            if from_unit in ["celsius", "fahrenheit"] and to_unit in ["celsius", "fahrenheit"]:
                converted_quantity = quantity.to(ureg(to_unit))
            else:
            
                converted_quantity = quantity.to(ureg(to_unit))

            embed = disnake.Embed(
                title="Temperature Conversion",
                description=(
                f"**{value} {from_unit.capitalize()}** ➡ **{converted_quantity.magnitude:.2f} {to_unit.capitalize()}**"
            ),
                color=disnake.Color.blue()
            )
            embed.set_footer(
                text=f"Requested by {inter.user}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None,
            )
            await inter.send(embed=embed)

        except Exception as e:
        
            embed = disnake.Embed(
                title="Error",
                description=f"An error occurred while converting temperature. {str(e)}",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Convert(bot))
