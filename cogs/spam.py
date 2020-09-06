import discord
import random
from discord.ext import commands
from discord import File, Message
from config import colors
import asyncio
import urllib.request

class spam_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def react(self, ctx, message: Message):
        await ctx.message.delete()
        await message.add_reaction("😳")
        await message.add_reaction("😷")
        await message.add_reaction("😈")
        await message.add_reaction("🤡")
        await message.add_reaction("👽")
        await message.add_reaction("👻")
        await message.add_reaction("☠️")
        await message.add_reaction("💀")
        await message.add_reaction("💩")
        await message.add_reaction("🥴")
        await message.add_reaction("🤤")
        await message.add_reaction("🟢")
        await message.add_reaction("⏱")
        await message.add_reaction("🤨")
        await message.add_reaction("🙃")
        await message.add_reaction("🤯")
        await message.add_reaction("🤭")
        await message.add_reaction("🤬")
        await message.add_reaction("🥶")
        await message.add_reaction("🥺")
        await message.add_reaction("👆")
        print ("Action Completed: react")

    @commands.command(pass_context=True)
    async def xpbot(self, ctx):
        await ctx.message.delete()
        print ("-stop to stop")
        print ("Action Started: xpbot")
        for i in range(9999):
            await ctx.send(".")
            await ctx.message.delete()
            print ("Sent Message")
            await asyncio.sleep(60)

    @commands.command(pass_context=True)
    async def spam(self, ctx, arg1):
        await ctx.message.delete()
        print ("Action Completed: spam")
        for i in range(9999):
            await ctx.send(arg1)
            await asyncio.sleep(0.7)

    @commands.command(pass_context=True)
    async def attachspam(self, ctx, arg1):
        await ctx.message.delete()
        await ctx.send("Downloading the requested img")
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached.png')
        print ("Action Completed: attachspam")
        for i in range(50):
            await ctx.send(file=File('./data/cached.png'))
            await asyncio.sleep(0.0)

    @commands.command(pass_context=True)
    async def mall(self, ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: mall")


def setup(bot: commands.Bot):
    bot.add_cog(spam_cog(bot))
