import random
import datetime

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context

class General(commands.Cog, name="General"):
    def __init__(self, bot) -> None:
        self.bot = bot
    @commands.hybrid_command(
        name="dm", description="Send Message to Person"
    )
    async def dm_sender(self, context: Context, user: discord.User,*,message) -> None:
        if user:
            embed = discord.Embed(
                title=f"Anda dapat salam dari {context.author.name}",
                description=f"{message}",
                color=0xBEBEFE,
            )
            embed.set_footer(text=f"Created at: {datetime.datetime.now()}")
            await user.send(embed=embed)
            await context.send('You dm has been sended')
        else:
            await context.send('You need to mention a user to send a DM.')


async def setup(bot) -> None:
    await bot.add_cog(General(bot))