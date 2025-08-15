import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# GitHub Secrets se API details lena
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Client setup
client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def main():
    # Example: apne aap ko message bhejna
    await client.send_message("me", "✅ GitHub Actions se script chal rahi hai!")

with client:
    client.loop.run_until_complete(main())
