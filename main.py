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
import json
import re
import requests
import aiohttp
import io
from colorama import Fore
from discord import File, Message
from discord.ext import commands
from discord.ext.commands import Bot
start_time = datetime.datetime.utcnow()

config = json.load(open('config.json', 'r'))

# <CONFIG> 
version = "1.2.0"
colors = [0x00f5b8, 0xe22400, 0x477015, 0xe9cb0c, 0x900ce9, 0x0cc8e9, 0x31e90c, 0x850ce9, 0x0c59e9, 0x02294b, 0x105035, 0x52e010, 0xfbff00, 0x0088ff, 0xff6600]
answers = ['Yes', 'No', 'Maybe']
changelog = f"{version}: Hybrid, works with or without heroku (thanks crafterpika!!!), Nitro Sniper (thanks crafterpika!)"
# <CONFIG> 
try:
    prefix = os.environ['PREFIX']
    token = os.environ['TOKEN']
    heroku = True
except KeyError:
    heroku = False
    config = json.load(open('config.json', 'r'))
    prefix = config["prefix"]
    token = config["token"]

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


# bot events
@bot.event
async def on_connect():
  print (f'Dwifte.PY {version}\nLogged in as: {bot.user}\nCurrent Prefix: {prefix}\n{changelog}\nMade by CrafterPika and DwifteJB')

#Bot Events
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

@bot.event
async def on_message(message):
	try:
		code = re.search(r'(discord.gift|discordapp.com/gifts)/\w{16,24}', message.content).group(0)
		if code:
			print("Nitro Code:", code)

			def returnData(status, code, value1, value2):
				if status == 'INVALID CODE' or 'DENIED':
					perhaps = Fore.RED
				elif status == 'ALREADY REDEEMED' or 'RATELIMITED' or 'UNKNOWN':
					perhaps = Fore.YELLOW
				else:
					perhaps = Fore.GREEN
				data = print(f'[{perhaps}{status}{Fore.RESET}] - [{Fore.CYAN}{code}{Fore.RESET}] - [{Fore.YELLOW}{value1}{Fore.RESET}] - [{Fore.YELLOW}{value2}{Fore.RESET}]')
				return data

			errors = {
      				1: '{"message": "Unknown Gift Code", "code": 10038}',
      				2: '{"message": "This gift has been redeemed already.", "code": 50050}',
      				3: 'You are being rate limited',
      				4: 'Access denied'
    			}
			payload = {
          			'channel_id': None,
          			'payment_source_id': None
        		}
			headers = {
      				'Content-Type': 'application/json',
      				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
      				'Authorization': config["token"]
    			}

			session = requests.Session()
			r = session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code.replace("discord.gift/", "")}/redeem', headers=headers, json=payload)
			if errors[1] in r.text:
				returnData('INVALID CODE', code, message.guild, message.author)
				open('nitro-logs.txt', 'a+').write(f'[WARN] Invalid Code {code} | {message.guild} | {message.author}'+'\n')
			elif errors[2] in r.text:
				returnData('ALREADY REDEEMED', code, message.guild, message.author)
				open('nitro-logs.txt', 'a+').write(f'[INFO] Already redeemed Code {code} | {message.guild} | {message.author}'+'\n')
			elif errors[3] in r.text:
				returnData('RATELIMITED', code, message.guild, message.author)
				open('nitro-logs.txt', 'a+').write(f'[WARN] RateLimited'+'\n')
			elif errors[4] in r.text:
				returnData('DENIED', code, message.guild, message.author)
				open('nitro-logs.txt', 'a+').write(f'[WARN] Denied'+'\n')
			else:
				returnData('CLAIMED', code, message.guild, message.author)
				open('nitro-logs.txt', 'a+').write(f'[INFO] Claimed Code {code} | {message.guild} | {message.author} | {r.text}'+'\n')

	except AttributeError:
            pass
	await bot.process_commands(message)

#cogs
bot.load_extension("cogs.general")
bot.load_extension("cogs.help")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.spam")
bot.load_extension("cogs.random")
bot.load_extension("cogs.ImgTools")

bot.run(token, bot=False) 
# speakl thanks to crafterpika for the help ;)