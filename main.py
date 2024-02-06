from decouple import config

from pyrogram import Client

API_ID = config("API_ID")
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")

PLUGINS = dict(root="plugins")

app = Client("app", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=PLUGINS)


if __name__ == "__main__":
    app.run()
 