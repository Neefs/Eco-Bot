from discord.ext import commands
from objects.discord_changes import Embed
import discord


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info(f"✅ {self.__class__.__name__} is ready!")


async def setup(bot):
    await bot.add_cog(Economy(bot))
