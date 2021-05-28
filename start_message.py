# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/dac37677227331b5a29f3.jpg"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓐𝓷𝓲𝓶𝓮 𝓢𝓽𝓮𝓻𝓪𝓶 𝓫𝓸𝓽, 𝓗𝓮𝓻𝓮 𝔂𝓸𝓾 𝓬𝓪𝓷 𝓓𝓸𝔀𝓷𝓵𝓸𝓪𝓭 𝓪𝓵𝓵 𝓐𝓷𝓲𝓶𝓮 𝓯𝓸𝓻 𝓕𝓡𝓔𝓔 😁

!!!  __𝓟𝓵𝓮𝓪𝓼𝓮 𝓻𝓮𝓪𝓭 𝓪𝓵𝓵 𝓽𝓱𝓮 𝓲𝓷𝓼𝓽𝓻𝓾𝓬𝓽𝓲𝓸𝓷𝓼 𝓪𝓫𝓸𝓾𝓽 𝓽𝓱𝓮 𝓫𝓸𝓽 𝓫𝓮𝓯𝓸𝓻𝓮 𝓼𝓾𝓻𝓯𝓲𝓷𝓰 𝓸𝓷...__  

𝓢𝓮𝓮 /whats_new 𝓽𝓸 𝓴𝓷𝓸𝔀 𝓪𝓫𝓸𝓾𝓽 𝓵𝓪𝓽𝓮𝓼𝓽 𝓾𝓹𝓭𝓪𝓽𝓮𝓼...""", reply_markup=reply_markup, parse_mode="markdown")
