import io
import aiohttp
import os
import urllib.request
import sys
import asyncio
import datetime
import pyfiglet
import discord
import random
from discord import File, Message
from discord.ext import commands
from discord.ext.commands import Bot
version = "release1.1"
start_time = datetime.datetime.utcnow()
try:
    prefix = os.environ['PREFIX']
    token = os.environ['TOKEN']
    heroku = True
except KeyError:
    heroku = False

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_connect():
  print (f'Dwifte.PY {version}\nLogged in as: {bot.user}\nCurrent Prefix: {prefix}')

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def say(ctx, arg1 = None, arg2 = None, arg3 = None, arg4 = None):
        if arg1 is None:
            arg1 = ""
        if arg2 is None:
            arg2 = "DwifteJB Rules"
        if arg3 is None:
            arg3 = ""
        if arg4 is None:
            arg4 = ""

        await ctx.message.delete()
        embed=discord.Embed(title=arg1, description=arg2, color=0xe22400)
        embed.set_thumbnail(url=arg4)
        embed.set_footer(text=arg3)
        await ctx.send(embed=embed)
        print ("Action Completed: say")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def kiss(ctx, user:discord.Member):
        await ctx.message.delete()
        embed=discord.Embed(title=f"{bot.user} kissed {user.name}", color=0xe22400)
        embed.set_thumbnail(url="https://media.tenor.com/images/a6669f4044d66658c7ce96be768965e4/tenor.gif")
        await ctx.send(embed=embed)
        
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def playing(ctx, arg1):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=arg1))
        await ctx.message.delete()

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def listening(ctx, arg1):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg1))
        await ctx.message.delete()

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def watching(ctx, arg1):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg1))
        await ctx.message.delete()
    
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def xpbot(ctx):
        await ctx.message.delete()
        print ("-stop to stop")
        print ("Action Started: xpbot")
        for i in range(9999):
            await ctx.message.delete()
            await ctx.send(".")
            await ctx.message.delete()
            await asyncio.sleep(60)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def react(ctx, message: Message):
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

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dmspam(ctx, user_id=None, *, args=None):
        if user_id != None and args != None:
            try:
                target = await bot.fetch_user(user_id)
                await ctx.message.delete()
                print ("Action Completed: dmspam")
                for i in range(9999):
                    await target.send(args)
                    await asyncio.sleep(0.7)
            except:
                await ctx.channel.send("Couldn't dm the given user.")

        else:
            await ctx.channel.send("You didn't provide a user's id and/or a message.")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def streaming(ctx, arg1):
        await bot.change_presence(activity = discord.Streaming(name = arg1, url = "https://twitch.tv/pornhub"))
        await ctx.message.delete()

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def spam(ctx, arg1):
        await ctx.message.delete()
        print ("Action Completed: spam")
        for i in range(9999):
            await ctx.send(arg1)
            await asyncio.sleep(0.7)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def stop(ctx):
        await ctx.message.delete()
        sys.exit()


    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def kall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: kall")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def purge(ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user.id).map(lambda m: m):
            try:
               await message.delete()
            except:
                pass
        print ("Action Completed: purge")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ball(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: ball")  

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def gp(ctx, mention = None):
        if mention is None:
            print ("User Didn't provide a mention")
        await ctx.message.delete()
        print ("Action Completed: gp")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ping(ctx):
        await ctx.message.delete()
        await ctx.send(f' 🏓 Pong! It took {round(bot.latency * 1000)}ms to contact Discord')
        print ("Action Completed: ping")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def help(ctx):
        await ctx.send("CONSOLE")
        print ("")
        print (f"{prefix}stop: Stops Bot")
        print (f"{prefix}ping: Shows PING")
        print (f"{prefix}download_png: Downloads Image")
        print (f"{prefix}xpbot: XP Bots")
        print (f"{prefix}ping: Shows PING")
        print (f"{prefix}attachspam: Spams Attachment")
        print (f"{prefix}spam: Spams selected message")
        print (f"{prefix}dmspam: Spams selected ID")
        print (f"{prefix}rall: Renamed everyone")
        print (f"{prefix}kall: Kicks Everyone")
        print (f"{prefix}ball: Bans Everyone")
        print (f"{prefix}dall: Deletes Every channel")
        print (f"{prefix}gp: Ghost Pings mention")
        print (f"{prefix}say: Shows an embed")
        print (f"{prefix}asay: Type in ascaii")
        print (f"{prefix}purge: Purges chat/select amount")
        print (f"{prefix}streaming: Show a streaming status")
        print (f"{prefix}playing: Show a playing status")
        print (f"{prefix}listening: Shows a listening status")
        print (f"{prefix}watching: Shows a watching status")
        print ("")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def rall(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: rall")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def mall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: mall")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def uptime(ctx):
        await ctx.message.delete()
        uptime = datetime.datetime.utcnow() - start_time
        uptime = str(uptime).split('.')[0]
        await ctx.send(f'I have been running for: '+uptime+'')

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dall(ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall all")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def avatar(ctx, *, user: discord.Member=None):
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

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def asay(ctx, arg1 = None):
        if arg1 is None:
            arg1 = "Hello World"
        ascii_banner = pyfiglet.figlet_format(arg1)
        await ctx.message.delete()
        await ctx.send(f'```{ascii_banner}```')
        print ("Action Completed: asay")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def destroy(ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: destroy")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def attachspam(ctx, arg1):
        await ctx.message.delete()
        await ctx.send("Downloading the requested img")
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached.png')
        print ("Action Completed: attachspam")
        for i in range(50):
            await ctx.send(file=File('./data/cached.png'))
            await asyncio.sleep(0.0)

    @bot.event
    async def on_message(message):
        if '<:yay:585696613507399692>   **GIVEAWAY**   <:yay:585696613507399692>' in message.content:
            await asyncio.sleep(random.randint(7,30))
            await message.add_reaction("🎉")
        await bot.process_commands(message)

    @bot.event
    async def on_message(message):
        if '<:Plasma1:714985504558415942> **GIVEAWAY** <:Plasma1:714985504558415942>' in message.content:
            await asyncio.sleep(random.randint(7,30))
            await message.add_reaction("🎉")
        await bot.process_commands(message)


except:
    pass
token = os.environ['TOKEN']
bot.run(token, bot=False)
