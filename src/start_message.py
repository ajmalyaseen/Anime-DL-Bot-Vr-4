# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [[
            InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("💡HELP", callback_data= "instructions")
            ],[
            InlineKeyboardButton("📕ABOUT", callback_data= "about"),
            InlineKeyboardButton("🔐 CLOSE", callback_data= "close")
            ]]
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/dac37677227331b5a29f3.jpg"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐚𝐧 𝐆𝐞𝐭 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐀𝐧𝐢𝐦𝐞 𝐚𝐧𝐝 𝐈𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐬 𝐅𝐑𝐄𝐄 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 𝐰𝐢𝐭𝐡 𝐚 𝐟𝐚𝐬𝐭𝐞𝐬𝐭 𝐬𝐞𝐫𝐯𝐞𝐫(𝐆𝐨𝐨𝐠𝐥𝐞 𝐝𝐫𝐢𝐯𝐞)""", reply_markup=reply_markup, parse_mode="markdown")
