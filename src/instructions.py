# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**help**

💡 /search  ᴀɴɪᴍᴇ ɴᴀᴍᴇ -> 𝘴𝘦𝘢𝘳𝘤𝘩  𝘢𝘯𝘪𝘮𝘦

💡 /airing -> 𝘎𝘦𝘵 𝘵𝘳𝘦𝘯𝘥𝘪𝘯𝘨 𝘈𝘯𝘪𝘮𝘦

💡 /genres -> get anime genres
**coderzHex**""", parse_mode="markdown", reply_markup=reply_markup)
