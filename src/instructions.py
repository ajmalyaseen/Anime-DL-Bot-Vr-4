# Copyright ยฉ 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    kkeeyyb = [
        [InlineKeyboardButton("โฌ๏ธBACK", callback_data=f"back"),InlineKeyboardButton("๐ABOUT", callback_data=f"about")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""

๐ฐ ๐๐๐ฌ๐ข๐ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ

/start - **แดสแดแดแด ษชา ษช แดแด แดสษชแด แด แดส ษดแดแด**

/help - **สแดสแดs สแดแด, สแดแดก แดแด แดsแด แดแด**

/info - **แดแด แดษดแดแดก แดสแดแดแด แดส แดแดสsแดษดแดส ษชษดาแดสแดแดแดษชแดษด** 

๐ฐ ๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐ ๐๐

โข /search  **แดษดษชแดแด ษดแดแดแด ->  ษขแดแด สแดแดส แดษดษชแดแด**

โข /genres -> **ษขแดแด แดษดษชแดแด ษขแดษดสแด**

โข /airing  ->  **ษขแดแด แดสแดษดแดษชษดษข แดษดษชแดแด**

๐ฐ ๐๐จ๐ง๐๐ญ๐ข๐จ๐ง๐ฌ

๐๐จ๐ง๐๐ญ๐ ๐ฎ๐ฌ ๐๐จ ๐ค๐๐๐ฉ ๐จ๐ฎ๐ซ ๐ฌ๐๐ซ๐ฏ๐ข๐๐๐ฌ ๐๐จ๐ง๐ญ๐ข๐ง๐ฎ๐จ๐ฎ๐ฌ ๐๐ฅ๐ข๐ฏ๐๐ข

๐ฒ๐จ๐ฎ ๐๐๐ง ๐ฌ๐๐ง๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ
๐จ๐ ๐๐๐ซ๐ฌ , ๐๐๐ซ๐ฌ, ๐๐๐ซ๐ฌ, ๐๐๐ซ๐ฌ, ๐๐๐๐ซ๐ฌ, ๐๐๐๐ซ๐ฌ 
 
**๐ฐFor Donate: DM @CoderzRoBot**

**[ยฉ๏ธแดแดแดแดสแดขสแดx](https://t.me/coderzHex)**""", reply_markup=reply_markup, parse_mode="markdown", disable_web_page_preview=True)
