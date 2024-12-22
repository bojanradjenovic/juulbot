import disnake
from disnake.ext import commands
from googletrans import Translator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.slash_command(description =  "Translate text to another language.")
    async def translate(self,
        inter: disnake.ApplicationCommandInteraction,
        text: str = commands.Param(description = "The text to translate"),
        source_lang: str = commands.Param(default="auto", description = "The source language (default: auto-detect)"),
        target_lang: str = commands.Param(default="en", description = "The target language (default: English)")):
        await inter.response.defer()
        try:
            translation = self.translator.translate(text, src=source_lang, dest=target_lang)
            embed = disnake.Embed(title="Translation", color=disnake.Color.blue())
            embed.add_field(name="Source language", value=translation.src, inline=True)
            embed.add_field(name="Target language", value=translation.dest, inline=True)
            embed.add_field(name="Original text", value=text, inline=False)
            embed.add_field(name="Translation", value=translation.text, inline=False)
            embed.set_footer(
                text=f"Requested by {inter.author}",
                icon_url=inter.author.avatar.url if inter.author.avatar else None
            )
            await inter.send(embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Translation",
                description=f"An error occurred: {e}",
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
def setup(bot):
    bot.add_cog(Translate(bot))
