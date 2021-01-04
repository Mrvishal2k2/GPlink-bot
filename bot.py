# Credits to mahesh malekar for his gplinks bot
# © Mrvishal
from os import environ
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')
AUTH_USERS = set(int(x) for x in environ.get("AUTH_USERS", "").split())


bot = Client('golinksrt bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.AUTH_USERS)
async def start(bot, message):
    
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm Golinksrt bot. Just send me link and get short link")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.AUTH_USERS)
async def link_handler(bot, message):

    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        button = [[InlineKeyboardButton("Link 🔗", url=short_link)]]
        markup = InlineKeyboardMarkup(button)
        await message.reply(f'Here is your shortlink \n`{short_link}`', reply_markup=markup, quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://golinksrt.xyz/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
