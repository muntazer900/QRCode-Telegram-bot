#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

import os
from pyrogram import Client, filters
from telegraph import upload_file
import pyqrcode
from messages import Msg
from bot.plugins.display.display_progress import progress


@Client.on_message(filters.text & filters.private)
async def qr_encode(client, message):
    qr = await client.send_message(
        chat_id=message.chat.id,
        text="جاري الكشف... 😁",
        reply_to_message_id=message.message_id
    )
    s = str(message.text)
    qrname = str(message.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale=6)
    img = qrname + '.png'
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"{Msg.error}")
        return
    try:
        await message.reply_photo(
            photo=img,
            progress=progress,
            progress_args=(
                "جاري التحميل....",
                qr
            )
        )

    except Exception as error:
        print(error)

    await qr.edit_text(f"https://telegra.ph{response[0]}")

    try:
        os.remove(img)
    except Exception as error:
        print('Something is {error}')
