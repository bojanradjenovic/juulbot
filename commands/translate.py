import disnake
from disnake.ext import commands
from deep_translator import GoogleTranslator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = GoogleTranslator(source='auto', target='en')

    @commands.slash_command(description="Translate text to another language.")
    async def translate(
        self,
        inter: disnake.ApplicationCommandInteraction,
        text: str = commands.Param(description="The text to translate"),
        source_lang: str = commands.Param(default="auto", description="The source language (default: auto-detect)"),
        target_lang: str = commands.Param(default="en", description="The target language (default: English)")
    ):
        await inter.response.defer()
        try:
            self.translator.source = source_lang
            self.translator.target = target_lang

            translated_text = self.translator.translate(text)

            embed = disnake.Embed(title="Translation", color=disnake.Color.blue())
            embed.add_field(name="Source language", value=source_lang, inline=True)
            embed.add_field(name="Target language", value=target_lang, inline=True)
            embed.add_field(name="Original text", value=text, inline=False)
            embed.add_field(name="Translated text", value=translated_text, inline=False)
            embed.set_footer(
                text=f"Requested by {inter.author}",
                icon_url=inter.author.avatar.url if inter.author.avatar else None
            )
            await inter.followup.send(embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Translation Error",
                description=f"An error occurred: {str(e)}",
                color=disnake.Color.red()
            )
            await inter.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(Translate(bot))
