# Copyright ยฉ 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("๐ชUPDATES", url="https://t.me/coderzHex"),InlineKeyboardButton("โป๏ธHELP", callback_data="instructions")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""**ABOUT ME**

โข ๐๐๐ฆ๐ : **[๐ฐ๐๐๐๐ ๐๐๐๐๐๐๐๐](http://t.me/Animesearcherpro_bot)** 

โข ๐๐๐ง๐ ๐ฎ๐๐ ๐ : **Payton** 

โข ๐๐ข๐๐ซ๐๐ซ๐ฒ : **Pyrogram**  

โข ๐๐๐ซ๐ฏ๐๐ซ :  **Heroku** 

โข ๐๐ญ๐๐ญ๐ฎ๐ฌ :  **V 1.0** 

โข ๐๐ซ๐๐๐ญ๐จ๐ซ : **[Mส.X](https://t.me/diago_x)**

**แดแดแดแดแดแดแด แดษด 2-6-21 ษชษดแดษชแดษด แดษชแดแด 7 :00 แดแด**

**[ยฉแดแดแดแดสแดขสแดx](https://t.me/coderzHex)**""", reply_markup=reply_markup, parse_mode="markdown", disable_web_page_preview=True)
