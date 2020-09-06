import aiohttp
import discord
import random
from discord.ext import commands
from discord import File, Message
from config import colors, answers, kiss, kiss_description, hug, hug_description

class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="8ball")
    async def eigth_ball(self, ctx, arg1):
        eigth_ball_embed=discord.Embed(color=random.choice(colors), description=random.choice(answers))
        await ctx.send(embed=eigth_ball_embed)

    @commands.command(pass_context=True)
    async def hug(self, ctx, user:discord.Member):
        await ctx.message.delete()
        embed=discord.Embed(title=f"{self.bot.user.name} hugged {user.name}", description=random.choice(hug_description), color=random.choice(colors))
        embed.set_image(url=random.choice(hug))
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def kiss(self, ctx, user:discord.Member):
        await ctx.message.delete()
        embed=discord.Embed(title=f"{self.bot.user.name} kissed {user.name}", description=random.choice(kiss_description), color=random.choice(colors))
        embed.set_image(url=random.choice(kiss))
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(general_cog(bot))
