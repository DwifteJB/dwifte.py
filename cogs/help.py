from discord.ext import commands
import json
import os

try:
    prefix = os.environ['PREFIX']
    heroku = True
except KeyError:
    heroku = False
    config = json.load(open('config.json', 'r'))
    prefix = config["prefix"]

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.send("CONSOLE")
        print ("")
        print (f"{prefix}stop: Stops Bot")
        print (f"{prefix}ping: Shows PING")
        print (f"{prefix}xpbot: XP Bots")
        print (f"{prefix}ping: Shows PING")
        print (f"{prefix}attachspam: Spams Attachment")
        print (f"{prefix}spam: Spams selected message")
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
        print (f"{prefix}uptime: Shows the time how long the bot is running.")
        print (f"{prefix}kiss: Kiss someone.")
        print (f"{prefix}hug: Hug someone.")
        print (f"{prefix}avatar: get someones avatar.")
        print (f"{prefix}8ball ['question']: says randomly yes or no or maybe")
        print ("---------------------------------------------------------------------")
        print (f"{prefix}size [img url]: makes images smaller")
        print (f"{prefix}cripsl [img url]: makes a img more weird/pixled")
        print (f"{prefix}invert [img url]: inverts a img")
        print (f"{prefix}grey_out [img url]: makes a img grey white")
        print (f"{prefix}combine [img url] [img you wanna paste into]: combines to imgs")

def setup(bot: commands.Bot):
    bot.add_cog(help_cog(bot))