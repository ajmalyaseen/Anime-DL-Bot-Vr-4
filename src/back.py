# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def back(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""start_message

""", parse_mode="markdown", reply_markup=reply_markup)
