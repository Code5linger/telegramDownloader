from telethon.sync import TelegramClient

# Replace your credentials
api_id = 29487448
api_hash = '0ecfdafe98927ff1aebfd88445ef9db1'
channel = 't.me/thanhxuan18c'

client = TelegramClient('scraper', api_id, api_hash)

with client:
    for message in client.iter_messages(channel, limit=10):
        if message.video:
            client.download_media(message.video, "downloads/")
            print("Downloaded:", message.video)
