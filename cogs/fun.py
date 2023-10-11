import aiohttp
import os
import requests
from bs4 import BeautifulSoup
import discord
import random
import youtube_dl
import json
from discord.ext import commands
from discord import File, Message
from config import colors, answers, kiss, kiss_description, hug, hug_description, funfact

try:
    prefix = os.environ['PREFIX']
    heroku = True
except KeyError:
    heroku = False
    config = json.load(open('config.json', 'r'))
    prefix = config["prefix"]

class fun_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="8ball")
    async def eigth_ball(self, ctx, *, arg1:str):
        eigth_ball_embed=discord.Embed(title=f"{arg1}", color=random.choice(colors), description=random.choice(answers))
        eigth_ball_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739435448203608134/754733857902952528/8-Ball.png")
        await ctx.send(embed=eigth_ball_embed)

    @commands.command(pass_context=True)
    async def http(self, ctx, arg1 = None):
        if arg1 is None:
            arg1 = "600"
        await ctx.message.delete()
        http = requests.post(f'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout={arg1}')
        f = open('data/http.txt', 'w')
        f.write(http.text)
        f.close()
        await ctx.send(file=discord.File('data/http.txt'))

    @commands.command(pass_context=True)
    async def fact(self, ctx):
        await ctx.message,delete()
        getfact= requests.get('https://useless-facts.sameerkumar.website/api').json()
        fact = getfact["data"]
        await ctx.send(fact)

    @commands.command(pass_context=True)
    async def blank(self, ctx):
        await ctx.message.delete()
        await ctx.send(" ** ** ")

    @commands.command(pass_context=True)
    async def sock5(self, ctx, arg1 = None):
        if arg1 is None:
            arg1 = "600"
        await ctx.message.delete()
        r = requests.post('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=600')
        f = open('data/sock5.txt', 'w')
        f.write(r.text)
        f.close()
        await ctx.send(file=discord.File('data/sock5.txt'))

    @commands.command(pass_context=True)
    async def youtube_dl(self, ctx, arg1):
        await ctx.message.delete()
        ydl_opts = {
            'outtmpl': os.path.join('./data/video.mp4'),
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([arg1])
        files = {
            'file': ('./data/video.mp4', open('./data/video.mp4', 'rb')),
        }
        response = requests.post('https://api.filepipe.io/upload.php', files=files)
        soup = BeautifulSoup(response.text, 'html.parser')
        row = soup.find('code')
        await ctx.send("Video Download:")
        await ctx.send(row.get_text())
        try:
            os.remove('./data/video.mp4')
        except:
            print("failed to delete the .mp4 trying again")
            await ctx.send(f"{prefix}delete_mp4")

    @commands.command(pass_context=True)
    async def delete_mp4(self, ctx):
        await ctx.message.delete()
        os.remove('./data/video.mp4')

    @commands.command(pass_through=True)
    async def tweet(self, ctx, arg1 = None, *, arg2 = None):
        if arg1 is None:
            arg1 = "CrafterPika"
        if arg2 is None:
            arg2 = "I am amazing, trust me."
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={arg1}&text={arg2}") as r:
                res = await r.json()
                await ctx.send(res["message"])

    @commands.command(pass_context=True)
    async def hug(self, ctx, user: discord.Member):
        await ctx.message.delete()
        if ctx.channel.type == discord.ChannelType.private:
            await ctx.send(f"Giving you a virtual hug\n{random.choice(hug_description)}\n{random.choice(hug)}")
        else:
            await ctx.send(f"{self.bot.user.name} hugged {user.name}\n{random.choice(hug_description)}\n{random.choice(hug)}")

    @commands.command(pass_context=True)
    async def kiss(self, ctx, user: discord.Member):
        await ctx.message.delete()
        print(f"{ctx.channel.type}\n{discord.ChannelType.private}")
        if ctx.channel.type == discord.ChannelType.private:
            await ctx.send(f"Giving you a virtual kiss\n{random.choice(kiss_description)}\n{random.choice(kiss)}")
        else:
            await ctx.send(f"{self.bot.user.name} kissed {user.name}\n{random.choice(kiss_description)}\n{random.choice(kiss)}")


async def setup(bot: commands.Bot):
    await bot.add_cog(fun_cog(bot))
