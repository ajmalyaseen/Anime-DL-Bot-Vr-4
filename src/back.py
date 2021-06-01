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
    query.edit_message_caption(caption="""
Hi {}!,

𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐚𝐧 𝐆𝐞𝐭 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐀𝐧𝐢𝐦𝐞 𝐚𝐧𝐝 𝐈𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐬 𝐅𝐑𝐄𝐄 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 𝐰𝐢𝐭𝐡 𝐚 𝐟𝐚𝐬𝐭𝐞𝐬𝐭 𝐬𝐞𝐫𝐯𝐞𝐫(𝐆𝐨𝐨𝐠𝐥𝐞 𝐝𝐫𝐢𝐯𝐞)...

 ©ᴄᴏᴅᴇʀᴢʜᴇx

""", parse_mode="markdown", reply_markup=reply_markup)
