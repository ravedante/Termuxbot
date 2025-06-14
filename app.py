from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 21545360
api_hash = "25343abde47196a7e4accaf9e6b03437"
bot_token = "7626520455:AAG7-nBNejByOECeuUIXAqACewGJlnfndQQ"

app = Client("file_id_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.video | filters.document)
async def get_file_id(client, message: Message):
    media = message.video or message.document
    if media:
        await message.reply_text(
            f"<b>Nome:</b> <code>{media.file_name}</code>\n"
            f"<b>File ID:</b> <code>{media.file_id}</code>\n"
            f"<b>Unique ID:</b> <code>{media.file_unique_id}</code>",
            parse_mode="html"
        )

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("Envie um vídeo ou documento para receber o file_id.")

app.run()
