from discord.ext import commands
from test import calculator
@commands.command()
async def calculate(ctx,*, arg):
    if arg == '':
        await ctx.send("FUCK YOU!")
    operation = "none"
    a = -1
    b = -1
    x = ''
    plus = arg.count('+')
    minus = arg.count('-')
    division = arg.count('/')
    multiplication = arg.count('*')
    if plus == 1 and minus == division == multiplication == 0:
        x = arg.split('+', 1)
        a = x[0]
        b = x[1]
        operation = "+"
    if minus == 1 and minus == division == multiplication == 0:
        x = arg.split('-', 1)
        a = x[0]
        b = x[1]
        operation = "-"
    if division == 1 and minus == division == multiplication == 0:
        x = arg.split('/', 1)
        a = x[0]
        b = x[1]
        operation = "/"
    if multiplication == 1 and minus == division == multiplication == 0:
        x = arg.split('*', 1)
        a = x[0]
        b = x[1]
        operation = "*"    
    await ctx.send(calculator(a,b,operation))


def setup(bot):
    bot.add_command(calculate)