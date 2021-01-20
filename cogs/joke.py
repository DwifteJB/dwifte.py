from discord.ext import commands
import pyjokes as pj 


class Jokes(commands.Cog):  
    def __init__(self, bot):  
        self.bot = bot

    @commands.command()  
    async def joke(self, ctx):  
        await ctx.send(pj.get_joke())  


def setup(bot): 
    bot.add_cog(Jokes(bot))  

#bad jokes but oh well
