# © Mrvishal2k2
#from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import requests
import aiohttp
'''
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')
YOUR_DOMAIN = environ.get('YOUR_DOMAIN')
'''
API_ID = 1648885
API_HASH = "978a4c44210cd6c4eb2db63674d1b98c"
BOT_TOKEN = "1222393558:AAHeO7A9u6sMoD5-UZ3Y665it_jE-frkStI"
API_KEY = "34NhlllUKloHINy31TpZThbqKd218Ylc"

YOUR_DOMAIN = "http://ramprasad2431.shortcm.li"



bot = Client('shorter',
	       api_id=API_ID,
	       api_hash=API_HASH,
	       bot_token=BOT_TOKEN,
	       workers=50,
	       sleep_threshold=10)

def get_shortlink(link):
    
    res = requests.post(
  'https://api.short.cm/links', { 
	'domain': YOUR_DOMAIN,
	'originalURL': link, },
	headers = {'authorization': API_KEY }, 
	json=True)
    res.raise_for_status()
    data = res.json()
    return data['shortURL']
'''

async def get_shortlink(link):
    url = 'https://api.short.cm/links'
    params = { 
	'domain': YOUR_DOMAIN,
	'originalURL': link, }
	
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params,headers = { 'authorization': API_KEY } ,raise_for_status=True) as response:
            data = await response.json()
            print(data)
            return data["shortUrl"]
            
'''
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply_text("Hello i am shortlink bot ",quote=True)

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    
    try:
        short_link = get_shortlink(link)
        button = [[InlineKeyboardButton("Link 🔗", url=short_link)]]
        markup = InlineKeyboardMarkup(button)
        await message.reply_text(f'The shortlink for link \n{link} \n is below 🥳  \n`{short_link}` ',reply_markup=markup, quote=True)
    except Exception as e:
        print(e)
        await message.reply(f'Error: {e}', quote=True)
'''
        
@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    
    try:
        res = requests.post(
  'https://api.short.cm/links', { 
	'domain': YOUR_DOMAIN,
	'originalURL': link, },
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)','authorization': API_KEY }, 
	json=True)
        res.raise_for_status()
        data = res.json()

        short_link = data["shortUrl"]
        button = [[InlineKeyboardButton("Link 🔗", url=short_link)]]
        markup = InlineKeyboardMarkup(button)
        await message.reply_text(f'The shortlink for link \n{link} \n is below 🥳  \n`{short_link}` ',reply_markup=markup, quote=True)
    except Exception as e:
        print(e)
        await message.reply(f'Error: {e}', quote=True)
'''
bot.run()
