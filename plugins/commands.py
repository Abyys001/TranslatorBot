from pyrogram import *


@Client.on_message(filters.command(["start"]))
async def start_command(client, message):
    await message.reply(
        "welcome to **TranslateBot**.\npaste farsi and i'll give you english.\nor paste english and i'll give you farsi :D",
        quote=True,
    )


