import aiohttp
import os
import requests
from bs4 import BeautifulSoup
import discord
import random
import youtube_dl
from discord.ext import commands
from discord import File, Message
from config import colors, answers, kiss, kiss_description, hug, hug_description, funfact

class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="8ball")
    async def eigth_ball(self, ctx, arg1):
        eigth_ball_embed=discord.Embed(color=random.choice(colors), description=random.choice(answers))
        await ctx.send(embed=eigth_ball_embed)

    @commands.command(pass_context=True)
    async def http(self, ctx, arg1 = None):
        if arg1 is None:
            arg1 = "600"
        await ctx.message.delete()
        http = requests.post(f'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout={arg1}')
        await ctx.send(f"HTTP Proxies, timeout = {arg1}")
        await ctx.send(http.text)
        print ("Sent http proxies,")
        print (http.text)
        
    @commands.command(pass_context=True)
    async def funfact(self, ctx):
        await ctx.message.delete()
        await ctx.send(random.choice(funfact))
    
    @commands.command(pass_context=True)
    async def blank(self, ctx):
        await ctx.message.delete()
        await ctx.send(" ** ** ")
        print ("Sent blank message ")
    
    @commands.command(pass_context=True)
    async def sock5(self, ctx, arg1 = None):
        if arg1 is None:
            arg1 = "600"
        await ctx.message.delete()
        r = requests.post('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=600')
        await ctx.send(f"Sock5 Proxies, timeout = {arg1}")
        await ctx.send(r.text)
    
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
        os.remove('./data/video.mp4')

    @commands.command(pass_through=True)
    async def tweet(self, ctx, arg1 = None, arg2 = None):
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
