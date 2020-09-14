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
        await ctx.message.delete()
        await ctx.send(f"**General Commands:**\n{prefix}stop (Stops the bot)\n{prefix}ping (Shows ping)\n{prefix}say (say something)\n{prefix}avatar (get a user avatar)\n{prefix}asay (Type in ascaii)\n{prefix}purge (Purges chat/select amount)\n{prefix}uptime (Shows the time how long the bot is running.)\n{prefix}info (shows a bit more infor about the bot.)\n{prefix}bitly (make bit.ly URLs)\n\n**Status Commands**:\n{prefix}streaming (Show a streaming status)\n{prefix}playing (Show a playing status)\n{prefix}listening (Shows a listening status)\n{prefix}watching (Shows a watching status)\n\n**Spam Command:**\n{prefix}spam (Self explanatory)\n{prefix}xpbot (Farm XP **(Broken as of rmay get fixed in the future)**)\n{prefix}attachspam (Spams Attachment)\n{prefix}gp (Ghost Pings mention)\n\n**Fun Commands:**\n{prefix}kiss (Kiss someone.)\n{prefix}hug (Hug someone.)\n{prefix}8ball (Eyyyy! It's 8ball)\n{prefix}youtube_dl (download yt vid)\n\n**Image Tools:**\n{prefix}size (makes images smaller)\n{prefix}cripsl (makes a img more weird/pixled)\n{prefix}invert (inverts a img)\n{prefix}grey_out (makes a img grey white)\n{prefix}combine [img url] [img you wanna paste into] (combines to imgs)\n{prefix}addtext_black (ads text to a pic (text color black))\n{prefix}addtext_white (ads text to a pic (text color white))\n{prefix}addtext_red (ads text to a pic (text color red))\n{prefix}gen_qr (make a simple QR code)\n\n**Random Commands:**\n{prefix}rall (Renames Everyone)\n{prefix}kall (Kicks Everyone)\n{prefix}ball (Bans Everyone)\n{prefix}dall (Deletes Every channel)\n{prefix}destroy (Destroys a whole server)")

def setup(bot: commands.Bot):
    bot.add_cog(help_cog(bot))
