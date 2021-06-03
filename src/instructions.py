# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    kkeeyyb = [
        [InlineKeyboardButton("⬇️BACK", callback_data=f"back"),InlineKeyboardButton("📕ABOUT", callback_data=f"about")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""

🔰 𝐁𝐚𝐬𝐢𝐜 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬

/start - **ᴄʜᴇᴄᴋ ɪғ ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ**

/help - **ʜᴇʟᴘs ʏᴏᴜ, ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ**

/about - **ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴍʏ ᴘᴇʀsᴏɴᴀʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ** 

🔰 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞

• /search  **ᴀɴɪᴍᴇ ɴᴀᴍᴇ ->  ɢᴇᴛ ʏᴏᴜʀ ᴀɴɪᴍᴇ**

• /genre -> **ɢᴇᴛ ᴀɴɪᴍᴇ ɢᴇɴʀᴇ**

• /airing  ->  **ɢᴇᴛ ᴛʀᴇɴᴅɪɴɢ ᴀɴɪᴍᴇ**

🔰 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧𝐬

𝐃𝐨𝐧𝐚𝐭𝐞 𝐮𝐬 𝐓𝐨 𝐤𝐞𝐞𝐩 𝐨𝐮𝐫 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐨𝐮𝐬 𝐚𝐥𝐢𝐯𝐞😢

𝐲𝐨𝐮 𝐜𝐚𝐧 𝐬𝐞𝐧𝐝 𝐚𝐧𝐲 𝐚𝐦𝐨𝐮𝐧𝐭
𝐨𝐟 𝟐𝟎𝐫𝐬 , 𝟑𝟎𝐫𝐬, 𝟓𝟎𝐫𝐬, 𝟕𝟎𝐫𝐬, 𝟏𝟎𝟎𝐫𝐬, 𝟐𝟎𝟎𝐫𝐬 
 
**💰For Donate: DM @CoderzRoBot**

**[©️ᴄᴏᴅᴇʀᴢʜᴇx](https://t.me/coderzHex)**""", reply_markup=reply_markup, parse_mode="markdown", disable_web_page_preview=True)
