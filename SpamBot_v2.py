import discord
from discord.ext import commands
import asyncio
import random
import pickle
import os
import pandas as pd 
from bs4 import BeautifulSoup
import requests

import os
data_path = 'C:/Users/DMoney/Desktop/Programming/Python/mtg_bot/'
os.chdir(data_path)

data = pd.read_pickle('./df_cards_war')

def get_image_from_card_name(name):
    '''
    This code will pull the name input from discord with no punctuation and spaces
    replaced by '-'' as:

    !ajanis-pridemate

    then check the local df/pickled df for the card name and pull the url. 
    Then grab the card image and embed it in discord chat.
    '''

    url = list(data.url)[int(data[data.name == name].index.values)]
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    cimg = [x['src'] for x in soup.find_all('img', {'class' : 'card war border-black'})][0]
    return cimg

client = discord.Client()
token = 'yourtokenhere'

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

    elif message.content.upper().startswith('!CARD'):
        args = message.content.split(' ')
        try:
            card_image = get_image_from_card_name(str(args[1]))
            e = discord.Embed(title = args[1])
            e.set_image(url = card_image)
            await message.channel.send(embed = e)

        except Exception:
            # await message.channel.send('Did you type it right?')
            return


client.run(token)

