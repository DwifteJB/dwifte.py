import io
import aiohttp
import os
import urllib
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
from config import version, changelog
start_time = datetime.datetime.utcnow()
 
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

url = 'http://dwifte.eu.org/config.json'
req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))


# bot events
@bot.event
async def on_connect():
  print (f'Dwifte.PY {version}\nLogged in as: {bot.user}\nCurrent Prefix: {prefix}\n\nChangelog:\n{changelog}\n\nMade by CrafterPika and DwifteJB')
  latestver = cont["latest"]
  if 130 == latestver:
      print("You are on the latest version!")
  else:
      print("WARNING: YOU ARE NOT ON THE LATEST VERSION!")

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
