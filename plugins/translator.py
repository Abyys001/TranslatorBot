from pyrogram import Client, filters

from googletrans import Translator
from langdetect import detect, detect_langs

translator = Translator()

fa = [
    "ur",
    "fa",
]

en = [
    "en",
    "fi",
    "nl",
]


@Client.on_message(filters.text & (~filters.command("start")), group=1)
async def translate(client, message):
    if detect(message.text) in fa:
        try:
            translated = translator.translate(message.text)
            await message.reply(translated.text, quote=True)
        except:
            await message.reply("SORRRY :( \nTry again....")
    elif detect(message.text) in en:
        try:
            translated = translator.translate(message.text, dest="fa")
            await message.reply(translated.text, quote=True)
        except:
            await message.reply("متاسفیم:( \nدوباره تلاش کن.....")
