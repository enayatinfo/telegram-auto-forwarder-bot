import os

from telethon import TelegramClient, events

api_id = '[api id]
api_hash = '[api hash]'
client = TelegramClient('anon', api_id, api_hash)

my_vip_channels = ['my_vip_channel1','my_vip_channel2','my_vip_channel3',]
target_channels = ['target_channel1','target_channel2',]


@client.on(events.NewMessage)
async def new_message_handler(event):
    # chat = await event.get_chat()
    # sender = await event.get_sender()
    chat_id = event.chat_id
    # sender_id = event.sender_id
    message_id = event.message.id
    # message_text = event.message.message
    if chat_id in target_channels:
        for vip in my_vip_channels:
            await client.forward_messages(vip, [message_id], chat_id)


client.start(phone='+989338033373')
client.run_until_disconnected()
