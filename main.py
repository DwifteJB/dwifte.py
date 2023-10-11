import io, os, urllib.request, sys, datetime, discord, random, json, re, requests, wget, shutil, zipfile, aiohttp, asyncio
from colorama import Fore
from discord import File, Message
from discord.ext import commands
from discord.ext.commands import Bot
from config import version, changelog
import repl
try:
	req = requests.get('https://raw.githubusercontent.com/DwifteJB/dwifte.py/master/data/update.json')
	cont = req.json()
except:
	print("[WARNING]: We couldn't check for a new update.")
	cont = json.loads(open("./data/update.json","r"))
config = json.load(open('config.json', 'r'))
try:
    prefix = os.environ['PREFIX']
    token = os.environ['TOKEN']
    heroku = True
except KeyError:
    heroku = False
    
    prefix = config["prefix"]
    token = config["token"]


bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


# bot events
if config["repl"] == True:
    repl.keep_alive()
@bot.event
async def on_connect():
  print (f'{Fore.RESET}{Fore.RED}Dwifte.PY {version}{Fore.RESET}\nLogged in as: {Fore.RED}{bot.user}\n{Fore.RESET}Current Prefix: {Fore.RED}{prefix}\n{Fore.CYAN}Made by Dwifte{Fore.RESET}')
  latestver = cont['latest']
  if latestver == version:
      pass
  else:
      features = cont['features']
      print (f"{Fore.RESET}{Fore.RED}Update {latestver} is available!\n{Fore.CYAN}Features: {features}\n Download at: github.com/DwifteJB/dwifte.py{Fore.RESET}")
      print("Launching Autoupdater")
      try:
          print("Trying to autoupdate")
          print("Grabbing latest zip from GH")
          wget.download("https://github.com/DwifteJB/dwifte.py/archive/master.zip", "./update.zip")
          print("Done")
          print("Removing old files")
          try:
              shutil.rmtree("cogs")
          except:
              pass

          try:
              shutil.rmtree("data")
          except:
              pass

          try:
              os.remove(".gitignore")
          except:
              pass

          try:
              os.remove("clear_heroku_files.sh")
          except:
              pass

          try:
              os.remove("app.json")
          except:
              pass

          try:
              os.remove("config.py")
          except:
              pass

          try:
              os.remove("main.py")
          except:
              pass

          try:
              os.remove("Procfile")
          except:
              pass

          try:
              os.remove("README.md")
          except:
              pass

          try:
              os.remove("requirements.txt")
          except:
              pass

          try:
              os.remove("update.json")
          except:
              pass
          print("Done")

          print("Updating files")
          with zipfile.ZipFile("update.zip", 'r') as zip_ref:
	          zip_ref.extractall("")

          main = os.getcwd()
          shutil.move("dwifte.py-master/cogs", f"{main}")
          shutil.move("dwifte.py-master/data", f"{main}")
          shutil.move("dwifte.py-master/config.py", f"{main}")
          shutil.move("dwifte.py-master/main.py", f"{main}")
          shutil.move("dwifte.py-master/app.json", f"{main}")
          shutil.move("dwifte.py-master/Procfile", f"{main}")
          shutil.move("dwifte.py-master/requirements.txt", f"{main}")
          print("Done!")

          print("Cleaning up")
          shutil.rmtree("dwifte.py-master")
          os.remove("update.zip")
          print("Done!\nPlease restart the bot!")

          print("Cleaning up")
          shutil.rmtree("dwifte.py-master")
          os.remove("update.zip")
          print("Done!\nPlease restart the bot!")
          os._exit(1)
      except:
          print("Update failed!")
          os._exit(1)

#Bot Events

@bot.event
async def on_message(message):
	try:
		code = re.search(r'(discord.gift|discordapp.com/gifts)/\w{16,24}', message.content).group(0)
		if code:
			print(f"{Fore.RESET}{Fore.RED}Nitro Code: {code} {Fore.RESET}")

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
      				'Authorization': token
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

	if '<:yay:585696613507399692>   **GIVEAWAY**   <:yay:585696613507399692>' in message.content:
		await asyncio.sleep(random.randint(7,30))
		await message.add_reaction("🎉")

	await bot.process_commands(message)

#cogs
async def load_cogs():
    print("loading cogs")
    try:
        await bot.load_extension("cogs.joke")
        await bot.load_extension("cogs.general")
        await bot.load_extension("cogs.help")
        await bot.load_extension("cogs.fun")
        await bot.load_extension("cogs.spam")
        await bot.load_extension("cogs.random")
        await bot.load_extension("cogs.ImgTools")
        print("cogs loaded")
    except Exception as e:
        print(f"could not load {e}")
        pass

asyncio.run(load_cogs())

bot.run(token)
