# Encoding = 'utf-8'| Mr.x
# Licensed under MIT License
# by coderzHex

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def back(client, callback_query):
    query = callback_query
    kkeeyyb = [
        [InlineKeyboardButton("ðªUPDATES", url="https://t.me/coderzHex"),InlineKeyboardButton("ðµââCREATOR", url="https://t.me/Diago_x")],
        [InlineKeyboardButton("â»ï¸HELP", callback_data="instructions"),InlineKeyboardButton("ðABOUT", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""**Heyð**,

ðð¡ð¢ð¬ ðð¨ð­ ððð§ ððð­ ð²ð¨ð®ð« ððð¯ð¨ð®ð«ð¢ð­ð ðð§ð¢ð¦ð ðð§ð ðð­ ð©ð«ð¨ð¯ð¢ððð¬ ðððð ðð¨ð°ð§ð¥ð¨ðð ðð¢ð§ð¤ ð°ð¢ð­ð¡ ð ððð¬ð­ðð¬ð­ ð¬ðð«ð¯ðð«(ðð¨ð¨ð ð¥ð ðð«ð¢ð¯ð)

NOTE :- CLICK THE HELP BUTTON TO KNOW MORE""", reply_markup=reply_markup, parse_mode="markdown")
