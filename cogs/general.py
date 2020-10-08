import discord
import random
from discord.ext import commands
from discord import File, Message
from config import colors, version
import sys
import aiohttp
import json
import io
import os
import datetime
import pyfiglet

start_time = datetime.datetime.utcnow()

try:
    prefix = os.environ['PREFIX']
    bitly_key = os.environ['bitly_key']
    heroku = True
except KeyError:
    heroku = False
    config = json.load(open('config.json', 'r'))
    bitly_key = config["bitly_key"]
    prefix = config["prefix"]

class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="say")
    async def say(self, ctx, arg1 = None, arg2 = None, arg3 = None, arg4 = None):
        if arg1 is None:
            arg1 = ""
        if arg2 is None:
            arg2 = ""
        if arg3 is None:
            arg3 = ""
        if arg4 is None:
            arg4 = ""

        await ctx.message.delete()
        embed=discord.Embed(title=arg1, description=arg2, color=random.choice(colors))
        embed.set_thumbnail(url=arg4)
        embed.set_footer(text=arg3)
        await ctx.send(embed=embed)
        print ("Action Completed: say")

    @commands.command(pass_context=True)
    async def playing(self, ctx, *, arg1:str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=arg1))
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def watching(self, ctx, *, arg1:str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg1))
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def listening(self, ctx, *, arg1:str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg1))
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def streaming(self, ctx, *, arg1:str):
        await self.bot.change_presence(activity = discord.Streaming(name = arg1, url = "https://twitch.tv/pornhub"))
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        await ctx.message.delete()
        sys.exit()

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *, user: discord.Member=None):
        await ctx.message.delete()
        format = "gif"
        user = user or ctx.author
        if user.is_avatar_animated() != True:
            format = "png"
        avatar = user.avatar_url_as(format = format if format != "gif" else None)
        async with aiohttp.ClientSession() as session:
            async with session.get(str(avatar)) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"Avatar.{format}"))

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        await ctx.message.delete()
        uptime = datetime.datetime.utcnow() - start_time
        uptime = str(uptime).split('.')[0]
        await ctx.send(f'I have been running for: '+uptime+'')

    @commands.command(pass_context=True)
    async def asay(self, ctx, *, arg1:str):
        if arg1 is None:
            arg1 = "Hello World"
        ascii_banner = pyfiglet.figlet_format(arg1)
        await ctx.message.delete()
        await ctx.send(f'```{ascii_banner}```')
        print ("Action Completed: asay")

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.message.delete()
        await ctx.send(f' 🏓 Pong! It took *{round(self.bot.latency * 1000)}ms* to contact Discord')
        print ("Action Completed: ping")

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user.id).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
        print ("Action Completed: purge")


    @commands.command(pass_context=True)
    async def tinyurl(self, ctx, *, link):
        url = f"http://tinyurl.com/api-create.php?url={link}"
        await ctx.send(url)
    @commands.command(pass_context=True)
    async def bitly(self, ctx, *, link):
        await ctx.message.delete()
        if bitly_key == '':
            print(f"[ERROR]: Bitly API Key was not found, please set it in config.json or the Heroku Settings (get one at bit.ly)")
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                        r = await req.read()
                        r = json.loads(r) 
                new = r['data']['url']
                await ctx.send(new)
            except Exception as e:
                print(f"[ERROR]:{e}")
            else:
                print(f"[ERROR]:{req.text}")

    @commands.command(pass_context=True)
    async def readall(self, ctx):
        await ctx.message.delete()
        for guild in self.bot.guilds:
            await guild.ack()

    @commands.command(pass_context=True)
    async def info(self, ctx):
        await ctx.message.delete()
        uptime = datetime.datetime.utcnow() - start_time
        uptime = str(uptime).split('.')[0]
        embed=discord.Embed(title=f"{self.bot.user.name} Info", description="Tells you info about you. Yes you.", color=random.choice(colors))
        embed.add_field(name="Uptime", value=f''+uptime+'', inline=False)
        embed.add_field(name="Prefix", value=f'{prefix}', inline=True)
        embed.add_field(name="Ping", value=f'{round(self.bot.latency * 1000)}ms', inline=True)
        embed.set_footer(text=f"Dwifte.PY | {version}")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(general_cog(bot))
