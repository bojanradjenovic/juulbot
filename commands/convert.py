import disnake
from disnake.ext import commands
import requests
from decimal import Decimal, ROUND_HALF_UP

class Convert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def convert(self, inter: disnake.ApplicationCommandInteraction):
        pass 


    @convert.sub_command()
    async def currency(
        self,
        inter: disnake.ApplicationCommandInteraction,
        from_currency: str = commands.Param(choices=["USD", "EUR", "GBP", "CAD", "DKK", "AED", "BGN", "RSD"], description="The currency to convert from"),
        to_currency: str = commands.Param(choices=["USD", "EUR", "GBP", "CAD", "DKK", "AED", "BGN", "RSD"], description="The currency to convert to"),
        amount: float = commands.Param(description="Amount to convert"),
    ):
        await inter.response.defer()
        
        cents = Decimal('0.01')
        rounded_amount = Decimal(amount).quantize(cents, ROUND_HALF_UP)

        api_url = (
            f"https://www.mastercard.co.uk/settlement/currencyrate/conversion-rate"
            f"?fxDate=0000-00-00&transCurr={from_currency}&crdhldBillCurr={to_currency}&bankFee=0&transAmt={rounded_amount}"
        )

        try:
            response = requests.get(api_url)
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
                color=disnake.Color.green()
            )
            embed.set_footer(
                text=f"Requested by {inter.user}",
                icon_url=inter.user.avatar.url if inter.user.avatar else None,
            )
            await inter.send(embed=embed)

        except Exception as e:
            embed = disnake.Embed(
                title="Error",
                description="An error occurred while fetching conversion rates. Please try again later.",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)


    @currency.error
    async def currency_error(self, inter: disnake.ApplicationCommandInteraction, error):
        embed = disnake.Embed(
            title="Currency Conversion Error",
            description=f"An error occurred: {error}",
            color=disnake.Color.red()
        )
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Convert(bot))
