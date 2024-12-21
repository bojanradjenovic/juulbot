import disnake
from disnake.ext import commands
import random

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="8ball", description="Ask the magic 8ball a question.")
    async def eightball(self, inter: disnake.ApplicationCommandInteraction, question: str):
        responses = [
            "Yes.",
            "No.",
            "Maybe.",
            "Definitely not.",
            "Ask again later.",
            "I have no idea.",
            "It's certain.",
            "Most likely.",
            "Outlook is good.",
            "Don't count on it."
        ]
        await inter.response.defer()
        response = random.choice(responses)
        embed = disnake.Embed(
                title="🎱 8Ball",
                description=f"**Answer:** {response}",
                color=disnake.Color.blue()
            )
        await inter.followup.send(embed=embed)
def setup(bot):
    bot.add_cog(EightBall(bot))