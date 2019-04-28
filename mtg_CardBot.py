###############################################################################
''' 
This code will pull the name input from discord with no punctuation and spaces
replaced by '-'' as:

!ajanis-pridemate

then check the local df/pickled df for the card name and pull the url. 
Then grab the card image and embed it in discord chat.

'''

import pandas as pd 
import numpy as np 
import re 
import requests
from bs4 import BeautifulSoup
import pickle
import discord
from discord.ext import commands
import asyncio

import os
data_path = 'C:/Users/DMoney/Desktop/Programming/Python/mtg_bot/'
os.chdir(data_path)

data = pd.read_pickle('./df_cards_war')

###############################################################################
#This code scrapes the card names for the War of the Spark set
# list_of_cards = [f'https://scryfall.com/card/war/{num}' for num in range(1,276)]

# names = []
# # get_names_from_url
# for url in list_of_cards:
#     # url = 'https://scryfall.com/card/war/1'
#     response = requests.get(url)
#     data = response.text
#     soup = BeautifulSoup(data, 'lxml')
#     tags = soup.find_all('a')

#     taglist = []
#     for tag in tags:
#         taglist.append(tag.get('href'))
#     names.append(taglist[13])

# card_names = [i.split('/')[-1] for i in names]
# card_num = [i.split('/')[-2] for i in names]
# card_set = [i.split('/')[-3] for i in names]

# d = {'name': card_names, 'num': card_num, 'set': card_set, 'url':names}
# df_cards_war = pd.DataFrame(data = d)
# #df_cards_war.to_pickle('./df_cards_war')
###############################################################################



