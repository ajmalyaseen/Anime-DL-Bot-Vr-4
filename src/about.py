# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def about(client, callback_query):
    query = callback_query
    kkeeyyb = [
        [InlineKeyboardButton("📪UPDATES", url="https://t.me/coderzHex"),InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/Diago_x")],
        [InlineKeyboardButton("♻️HELP", callback_data="instructions"),InlineKeyboardButton("📕ABOUT", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(text="""

 **About Me**

• 𝐍𝐚𝐦𝐞 : Anime_DL 

• 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : ᴘᴀʏᴛᴏɴ 

• 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : ᴘʏʀᴏɢʀᴀᴍ 

• 𝐒𝐞𝐫𝐯𝐞𝐫 :  ʜᴇʀᴏᴋᴜ 

• 𝐒𝐭𝐚𝐭𝐮𝐬 :  V 1.0 

• 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : ᴅɪᴀɢᴏ

**ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 1-6-21 ɪɴᴅɪᴀɴ ᴛɪᴍᴇ 7 :00 ᴘᴍ**

**©ᴄᴏᴅᴇʀᴢʜᴇx**""", reply_markup=reply_markup, parse_mode="markdown")
