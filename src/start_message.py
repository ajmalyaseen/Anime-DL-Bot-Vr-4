# Copyright Â© 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("ðªUPDATES", url="https://t.me/coderzHex"),InlineKeyboardButton("ðµââCREATOR", url="https://t.me/Diago_x")],
        [InlineKeyboardButton("â»ï¸HELP", callback_data="instructions"),InlineKeyboardButton("ðABOUT", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    message.reply_text(f"""**Heyð {message.chat.first_name}**,

ðð¡ð¢ð¬ ðð¨ð­ ððð§ ððð­ ð²ð¨ð®ð« ððð¯ð¨ð®ð«ð¢ð­ð ðð§ð¢ð¦ð ðð§ð ðð­ ð©ð«ð¨ð¯ð¢ððð¬ ðððð ðð¨ð°ð§ð¥ð¨ðð ðð¢ð§ð¤ ð°ð¢ð­ð¡ ð ððð¬ð­ðð¬ð­ ð¬ðð«ð¯ðð«(ðð¨ð¨ð ð¥ð ðð«ð¢ð¯ð)

NOTE :- CLICK THE HELP BUTTON TO KNOW MORE""", reply_markup=reply_markup, parse_mode="markdown")
