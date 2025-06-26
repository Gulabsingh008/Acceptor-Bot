import os
import threading
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from flask import Flask

# Flask health check server
app = Flask(__name__)

@app.route('/')
def index():
    return "TechVJ Bot is Alive!"
def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Pyrogram Bot class
class Bot(Client):
    def __init__(self):
        super().__init__(
            "vj join request bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print('✅ Bot Started Powered By Mhakal')

    async def stop(self, *args):
        await super().stop()
        print('🛑 Bot Stopped. Bye!')

if __name__ == "__main__":
    # 🟢 Start Flask in background thread
    threading.Thread(target=run_flask).start()

    # 🟢 Start the bot
    Bot().run()
