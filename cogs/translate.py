from discord.ext import commands
import discord
from textblob import TextBlob
import requests
import goslate

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        bot = self.bot
        config = self.bot.config
        if message.author != bot.user:
            b = TextBlob(message.content)
            lang = b.detect_language()
            if lang == "tr":
                t = b.translate(to='ru')
                embed = discord.Embed(description=f"{t}", color=0x03fc28)
                embed.set_footer(text="Türkçe (TR) > Russian (RU)")
            elif lang == "ru":
                t = b.translate(to='tr')
                embed = discord.Embed(description=f"{t}", color=0x03fc28)
                embed.set_footer(text="Russian (RU) > Türkçe (TR)")
            await message.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(Chat(bot))