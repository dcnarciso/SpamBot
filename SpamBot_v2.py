import discord
from discord.ext import commands
import asyncio
import random
from bs4 import BeautifulSoup
import requests

# data = pd.read_pickle('./df_cards_war')

client = discord.Client()
token = 'MzkzOTE0MzA4NTgyNTcyMDMy.DR8s6A.z3u8Hrp4T_GD74HxgCMp7-iuYBM'

bot = discord.ext.commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='HUMAN EXTINCTION'))

@client.event
async def on_message(message):

    if message.content.upper().startswith('!FLIP'):
        flip = random.choice(['Heads', 'Tails'])
        await message.channel.send(flip)

    elif message.content.upper().startswith('DANNY'):
        await message.channel.send(':thumbsup:')

    elif message.content.upper().startswith('!GTFO'):
        #if message.author.id == '172720442723794944': #'172720442723794944'
        await client.close()
        await client.logout()
        # else:
        #     #userID = message.author.id
        #     await message.channel.send(f"I'm sorry <@{userID}>, I'm afraid I can't do that, bro.")

    elif message.content.upper().startswith('!CATS'):
        e = discord.Embed()
        e.set_image(url = 'https://s-i.huffpost.com/gen/3152148/images/o-ANIMALS-FUNNY-facebook.jpg')
        await message.channel.send(embed = e)

    elif message.content.upper().startswith('!MEMBERS'):
        x = len(message.server.members)
        await message.channel.send(f"There are {x} members on this server")

    elif message.content.upper().startswith('!SAY'):
        args = message.content.split(' ')
        await message.channel.send("%s" % (" ".join(args[1:])))

    elif message.content.upper().startswith('!ROLL'):
        args = message.content.split(' ')
        try:
            rolls, limit = map(int, args[1].split('d'))
        except Exception:
            
            await message.channel.send('Must be NdN, stupid!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await message.channel.send(result)

    elif message.content.upper().startswith('!GAME'):
        args = message.content.split(' ')
        try:
            await client.change_presence(activity=discord.Game(name=(" ".join(args[1:]))))
        except Exception:
            await message.channel.send('Not a valid game, bro.')
            return

    elif message.content.upper().startswith('!YGO'):
        args = message.content.split(' ')
        try:
            name_you_type = ' '.join(args[1:])
            url = 'https://db.ygoprodeck.com/api/v4/cardinfo.php?name=' + name_you_type
            r = requests.get(url).json()
            card_image = r[0][random.randint(0,len(r[0])-1)]['image_url']

            e = discord.Embed(title = 'Is this your card?\n' + name_you_type)
            e.set_image(url = card_image)
            await message.channel.send(embed = e)

        except Exception:
            return

    elif message.content.upper().startswith('!MTG'):
        args = message.content.split(' ')
        try:
            name_you_type = ' '.join(args[1:])
            url = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?name=' + name_you_type
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            card_image = 'https://gatherer.wizards.com/' + [x['src'] for x in soup.find_all('img')][2].split('../../')[1]

            e = discord.Embed(title = 'Is this your card?\n' + name_you_type)
            e.set_image(url = card_image)
            await message.channel.send(embed = e)

        except Exception:
            return

client.run(token)

