from PIL import Image, ImageFilter, ImageFont, ImageDraw
import PIL.ImageOps
import os
import urllib.request
from discord import File
from discord.ext import commands
import qrcode

class ImgTools_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def size(self, ctx, arg1):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        re_size = (300, 300)
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
            maniplulate = Image.open('./data/cached2.png')
            maniplulate.thumbnail(re_size)
            maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("An HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def cripsl(self, ctx, arg1):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
            maniplulate = Image.open('./data/cached2.png')
            maniplulate.convert("RGBA")
            datas = maniplulate.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    if item[0] > 150:
                        newData.append((0, 0, 0, 255))
                    else:
                        newData.append(item)
                        print(item)
            maniplulate.putdata(newData)
            maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("An HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def invert(self, ctx, arg1):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
        	maniplulate = Image.open('./data/cached2.png')
        	inverted_image = PIL.ImageOps.invert(maniplulate)
        	inverted_image.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("An HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def grey_out(self, ctx, arg1):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
        	maniplulate = Image.open('./data/cached2.png').convert('LA')
        	maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("And HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def combine(self, ctx, arg1, arg2):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        url2 = arg2
        urllib.request.urlretrieve(url, './data/cached2.png')
        urllib.request.urlretrieve(url2, './data/cached3.png')
        try:
            Image1 = Image.open('./data/cached2.png')
            Image2 = Image.open('./data/cached3.png')

            size = print(type(Image2.size))

            area = (size)
            Image1.paste(Image2, area)
            Image1.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("And HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')
        os.remove('./data/cached3.png')

    @commands.command(pass_context=True)
    async def clear_img_cache(self, ctx, arg1, arg2):
        await ctx.message.delete()
        os.remove('./data/cached2.png')
        try:
        	os.remove('./data/cached3.png')
        	os.remove('./data/maniplulated.png')
        except FileNotFoundError:
        	pass

    @commands.command(pass_context=True)
    async def addtext_black(self, ctx, arg1, arg2):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
            maniplulate = Image.open('./data/cached2.png')
            draw = ImageDraw.Draw(maniplulate)
            font = ImageFont.truetype("./data/arial.ttf", 32)
            draw.text((0, 0),arg2,(0, 0, 0),font=font)
            maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("And HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def addtext_white(self, ctx, arg1, arg2):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
            maniplulate = Image.open('./data/cached2.png')
            draw = ImageDraw.Draw(maniplulate)
            font = ImageFont.truetype("./data/arial.ttf", 32)
            draw.text((0, 0),arg2,(255, 255, 255),font=font)
            maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("And HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def addtext_red(self, ctx, arg1, arg2):
        await ctx.message.delete()
        print('Downloading Requested file')
        url = arg1
        urllib.request.urlretrieve(url, './data/cached2.png')
        try:
            maniplulate = Image.open('./data/cached2.png')
            draw = ImageDraw.Draw(maniplulate)
            font = ImageFont.truetype("./data/arial.ttf", 32)
            draw.text((0, 0),arg2,(255, 0, 0),font=font)
            maniplulate.save('./data/maniplulated.png')
        except NotImplementedError:
            print("It seems like the image you are using is not supported!")
            return False
        except OSError:
            print("This image is bad")
            return False
        except HTTPError:
            print("And HTTP Error Occured")
            return False
        await ctx.send(file=File('./data/maniplulated.png'))
        os.remove('./data/maniplulated.png')
        os.remove('./data/cached2.png')

    @commands.command(pass_context=True)
    async def gen_qr(self, ctx, arg1):
        await ctx.message.delete()
        qr = qrcode.make(arg1)
        qr.save('./data/gen_qr.png')
        await ctx.send(file=File('./data/gen_qr.png'))
        os.remove('./data/gen_qr.png')


def setup(bot: commands.Bot):
    bot.add_cog(ImgTools_cog(bot))
