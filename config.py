import os
import json

config = json.load(open('config.json', 'r'))

try:
    prefix = os.environ['PREFIX']
    heroku = True
except KeyError:
    heroku = False
    prefix = config["prefix"]

version = "1.3.0"
changelog ="- Uses now cogs\n-Added Nitro Sniper\n-New Commands POG\nNow supports heroku/non-heroku"
colors = [0x00f5b8, 0xe22400, 0x477015, 0xe9cb0c, 0x900ce9, 0x0cc8e9, 0x31e90c, 0x850ce9, 0x0c59e9, 0x02294b, 0x105035, 0x52e010, 0xfbff00, 0x0088ff, 0xff6600]
answers = ['🎱 | Yes', '🎱 | No', '🎱 | Maybe', '🎱 | Try again later']
kiss = ['https://media.tenor.com/images/a6669f4044d66658c7ce96be768965e4/tenor.gif', 'https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif', 'https://media1.tenor.com/images/0ec5382910e34ca5649f6c328124daa1/tenor.gif', 'https://media.tenor.com/images/346f1960b45e29861304b867faf24f86/tenor.gif', 'https://media1.tenor.com/images/1d05ed38dace67c8912a14e963afd0e9/tenor.gif']
kiss_description = ['How Cute 🧡', 'OwO a kiss 😘', '😳']
hug = ['https://acegif.com/wp-content/uploads/anime-hug.gif', 'https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif', 'https://acegif.com/wp-content/gif/anime-hug-79.gif', 'https://media1.tenor.com/images/f20151a1f7e003426ca7f406b6f76c82/tenor.gif', 'https://media1.tenor.com/images/fd47e55dfb49ae1d39675d6eff34a729/tenor.gif']
hug_description = ['Awwww 🥰', 'A Hug OwO 💘', '🥵']
