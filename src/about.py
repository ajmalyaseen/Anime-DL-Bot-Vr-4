# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def about(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("📪UPDATES", url="https://t.me/coderzHex"),InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/Diago_x")],
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""

 **About Me**

• 𝐍𝐚𝐦𝐞 : Anime_DL 

• 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : ᴘᴀʏᴛᴏɴ 

• 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : ᴘʏʀᴏɢʀᴀᴍ 

• 𝐒𝐞𝐫𝐯𝐞𝐫 :  ʜᴇʀᴏᴋᴜ 

• 𝐒𝐭𝐚𝐭𝐮𝐬 :  V 1.0 

• 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : ᴅɪᴀɢᴏ

**ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 1-6-21 ɪɴᴅɪᴀɴ ᴛɪᴍᴇ 7 :00 ᴘᴍ**

**©ᴄᴏᴅᴇʀᴢʜᴇx**""", parse_mode="markdown", reply_markup=reply_markup)
