import discord
import logging
import requests
from discord.ext import commands
from decimal import Decimal, ROUND_HALF_UP
logger = logging.getLogger('discord.ext')

@commands.command()
async def currency(ctx, amount: float, input, output):
    logger.info(f"{ctx.author.name}#{ctx.author.discriminator} has ran '{ctx.command}' in guild '{ctx.guild}' with message '{ctx.message.content}'!\n")
    cents = Decimal('0.01')
    uri = "https://www.mastercard.co.uk"
    amount = Decimal(amount).quantize(cents, ROUND_HALF_UP)
    
    def convertcurrency(amount: Decimal, input, output):
            req = f"{uri}/settlement/currencyrate/conversion-rate?fxDate=0000-00-00&transCurr={input}&crdhldBillCurr={output}&bankFee=0&transAmt={amount}"
            resp = requests.request("GET", req)
            if resp.status_code == 200:
                return resp.json()
            else:
                return False
    conversion = convertcurrency(amount, input, output)
    if conversion == False:
        await ctx.send(f"Error! Unable to get conversion rate. Please try again later.")
        return
    
    convamount = Decimal(conversion['data']['transAmt']).quantize(cents, ROUND_HALF_UP)
    outputamount = Decimal(conversion['data']['crdhldBillAmt']).quantize(cents, ROUND_HALF_UP)
    embed=discord.Embed(title=f"Currency conversion!")
    embed.description = f"{convamount} {input.upper()} --> {outputamount} {output.upper()}"
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = ctx.author.colour
    await ctx.send(embed=embed)

@currency.error
async def currency_error(ctx, error):
    embed=discord.Embed(title=f"Currency conversion!")
    embed.description = f"Unable to convert currency! (Wrong input)"
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.colour = ctx.author.colour
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(currency)