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
        [InlineKeyboardButton("⬇️BACK", callback_data=f"back"),InlineKeyboardButton("♻️HELP", callback_data=f"instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""**ABOUT ME**

• 𝐍𝐚𝐦𝐞 : **[𝙰𝚗𝚒𝚖𝚎 𝚂𝚎𝚊𝚛𝚌𝚑𝚎𝚛](http://t.me/Animesearcherpro_bot)** 

• 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : **Payton** 

• 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : **Pyrogram**  

• 𝐒𝐞𝐫𝐯𝐞𝐫 :  **Heroku** 

• 𝐒𝐭𝐚𝐭𝐮𝐬 :  **V 1.0** 

• 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : **[Mʀ.X](https://t.me/diago_x)**

**ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 2-6-21 ɪɴᴅɪᴀɴ ᴛɪᴍᴇ 7 :00 ᴘᴍ**

**[©ᴄᴏᴅᴇʀᴢʜᴇx](https://t.me/coderzHex)**""", reply_markup=reply_markup, parse_mode="markdown", disable_web_page_preview=True)
