import os
# CONFIG
# ---------
prefix = "-"
# ----------

import urllib.request
import sys
import asyncio
import pyfiglet
import discord
from discord import File, Message
from discord.ext import commands
from discord.ext.commands import Bot
from discord_webhook import DiscordWebhook, DiscordEmbed

try:
    token = os.environ['TOKEN']
    heroku = True
except KeyError:
    heroku = False

# Imports the needed libs.
print ("Loading..")
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
# Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself.

@bot.event
async def on_ready():
    print ("It's time.")
# Prints when the bot is ready to be used.

@bot.event
async def on_connect():
  webhook = DiscordWebhook(url='https://discord.com/api/webhooks/748244489822273707/wNvSWyi1UomwwvwmJgT-tyNjBzuP0NgNuxsqE8CDFs2FgEIo2fbFLLwCKgpr5PUL--9J')
  # create embed object for webhook
  embed = DiscordEmbed(title='DwifteJB Online', description='Back online', color=242424)
  # add embed object to webhook
  webhook.add_embed(embed)
  response = webhook.execute()
  # changelog
  webhook = DiscordWebhook(url='https://discord.com/api/webhooks/748244489822273707/wNvSWyi1UomwwvwmJgT-tyNjBzuP0NgNuxsqE8CDFs2FgEIo2fbFLLwCKgpr5PUL--9J')
  # create embed object for webhook
  embed = DiscordEmbed(title='Changelog', description='something was added', color=242424)
  # add embed object to webhook
  webhook.add_embed(embed)
  response = webhook.execute()

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False
    # A secondary check to ensure nobody but the owner can run these commands. Commented out for performance

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
        print ("-restart to stop")
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

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dmspam(ctx, user_id=None, *, args=None):
        if user_id != None and args != None:
            try:
                target = await bot.fetch_user(user_id)
                await ctx.message.delete()
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
        for i in range(9999):
            await ctx.send(arg1)
            await asyncio.sleep(0.7)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def restart(ctx):
        await ctx.message.delete()
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/748244489822273707/wNvSWyi1UomwwvwmJgT-tyNjBzuP0NgNuxsqE8CDFs2FgEIo2fbFLLwCKgpr5PUL--9J')
        embed = DiscordEmbed(title='DwifteJB is manually Restarting', description='Restart in progress', color=242424)
        webhook.add_embed(embed)
        response = webhook.execute()
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
    # Kicks every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def download_png(ctx, arg1):
        await ctx.message.delete()
        #download png
        os.remove("./data/png.png")
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/png.png')
        #attach it
        await ctx.send(file=File('./data/png.png'))

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def purge(ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user.id).map(lambda m: m):
            try:
               await message.delete()
            except:
                pass

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
    # Bans every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def gp(ctx, mention = None):
        if mention is None:
            print ("User Didn't provide a mention")
        await ctx.message.delete()

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ping(ctx):
        await ctx.message.delete()
        await ctx.send(f' 🏓 Pong! It took {round(bot.latency * 1000)}ms to contact Discord')

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def help(ctx):
        await ctx.send("lol check console")
        print ("Help command is now here due to bannings from embeds.")
        print ("")
        print ("-ping: Shows PING")
        print ("-download_png: Downloads Image")
        print ("-xpbot: XP Bots")
        print ("-ping: Shows PING")
        print ("-attachspam: Spams Attachment")
        print ("-spam: Spams selected message")
        print ("-dmspam: Spams selected ID")
        print ("-rall: Renamed everyone")
        print ("-kall: Kicks Everyone")
        print ("-ball: Bans Everyone")
        print ("-dall: Deletes Every channel")
        print ("-gp: Ghost Pings mention")
        print ("-say: Shows an embed")
        print ("-asay: Type in ascaii")
        print ("-purge: Purges chat/select amount")
        print ("-streaming: Show a streaming status")
        print ("-playing: Show a playing status")
        print ("-listening: Shows a listening status")
        print ("-watching: Shows a watching status")
        print ("")

#    @commands.check(self_check)
#    @bot.command(pass_context=True)
#    async def ehelp(ctx, arg1 = None):
#        if arg1 is help:
#            embed=discord.Embed(title="DwifteJB SelfBot ;)", description="Here you can seek help with commands ;)")
#            embed.add_field(name="Command Info", value="Shows you all the commands", inline=True)
#            embed.add_field(name="Permissions Needed", value="NONE", inline=True)
#            embed.set_footer(text="Only you can execute ;)")
#            await ctx.send(embed=embed)
#        if arg1 is None:
#            embed=discord.Embed(title="DwifteJB SelfBot ;)", description="Here you can seek help with commands ;)")
#            embed.add_field(name="-help", value="Shows this UI", inline=True)
#            embed.add_field(name="-ping", value="Shows your PING", inline=True)
#            embed.add_field(name="-rall {'name here'}", value="Renames everyone ", inline=True)
#            embed.add_field(name="-ball", value="Bans Everyone", inline=True)
#            embed.add_field(name="-kall", value="Kicks Everyone", inline=True)
#            embed.add_field(name="-dall", value="Deletes all channels", inline=True)
#            embed.add_field(name="-destroy", value="Destroys a server", inline=True)
#            embed.add_field(name="-say", value="Embeds Message", inline=True)
#            embed.add_field(name="-restart", value="Restarts Bot", inline=True)
#            embed.add_field(name="-gp", value="Instant GhostPing", inline=True)
#            embed.add_field(name="-asay", value="Ascaii ;)", inline=True)
#            embed.add_field(name="-purge", value="Purge's your messages", inline=True)
#            embed.add_field(name="-spam", value="spam spam", inline=True)
#            embed.add_field(name="-attachspam", value="Spams attachments", inline=True)
#            embed.add_field(name="-dmspam", value="spams IDs dms", inline=True)
#            embed.add_field(name="-streaming", value="Sets your streaming Status", inline=True)
#            embed.add_field(name="-playing", value="Sets your playing Status", inline=True)
#            embed.add_field(name="-watching", value="Sets your watching Status", inline=True)
#            embed.add_field(name="-listening", value="Sets your listening Status", inline=True)
#            embed.set_footer(text="Only you can execute ;)")
#            await ctx.send(embed=embed)
#        await ctx.message.delete()

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
    # Renames every member in a server.

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
    # Messages every member in a server.

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
    # Can perform multiple actions that envolve mass deleting.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def asay(ctx, arg1 = None):
        if arg1 is None:
            arg1 = "Hello World"
        ascii_banner = pyfiglet.figlet_format(arg1)
        await ctx.message.delete()
        await ctx.send(f'```{ascii_banner}```')
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
    # Outright destroys a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def attachspam(ctx):
        await ctx.message.delete()
        for i in range(9999):
            await ctx.send(file=File("./data/png.png"))
            await asyncio.sleep(0.0)

    @bot.event
    async def on_message(message):
        if 'Congratulations <@!521762564062052393>' in message.content:
            print ("WON GIVEAWAY BUT WEBHOOK IS SHit")
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/748244489822273707/wNvSWyi1UomwwvwmJgT-tyNjBzuP0NgNuxsqE8CDFs2FgEIo2fbFLLwCKgpr5PUL--9J', content=f'***GIVEAWAY WON***\n\nIn Server: {message.guild}/nIn Channel: {message.channel}')
            response = webhook.execute()
        await bot.process_commands(message)

    @bot.event
    async def on_message(message):
        if '<:yay:585696613507399692>   **GIVEAWAY**   <:yay:585696613507399692>' in message.content:
            await asyncio.sleep(7)
            await message.add_reaction("🎉")
        await bot.process_commands(message)

except:
    pass
print("")
print("")
print("BOT LOADED :)")
print("")
print("")
print("Commands:")
print("rall : Renames all")
print("ball : Bans all")
token = os.environ['TOKEN']
bot.run(token, bot=False)
# Starts the bot by passing it a token and telling it it isn't really a bot.