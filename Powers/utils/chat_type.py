from Powers.bot_class import Gojo

from pyrogram.enums import ChatType
from pyrogram.types import Message



async def chattype(m: Message):
    if bool(m.chat and m.chat.type in {ChatType.CHANNEL}):
        ct = "channel"
    
    if bool(m.chat and m.chat.type in {ChatType.PRIVATE}):
        ct = "private"

    if bool(m.chat and m.chat.type in {ChatType.SUPERGROUP}) or bool(m.chat and m.chat.type in {ChatType.GROUP}):
        ct = "supergroup"

    if bool(m.chat and m.chat.type in {ChatType.BOT}):
        ct ="bot"


    return ct

async def c_type(chat_id):
    c = Gojo.get_chat(chat_id)
    mem = Gojo.get_chat_members_count(chat_id)
    
    if c.type == ChatType.BOT:
        ct = "bot"
    
    if c.type == ChatType.CHANNEL:
        ct = "channel"
    
    if c.type == ChatType.GROUP:
        ct = "group"
    
    if c.type == ChatType.SUPERGROUP:
        ct = "supergroup"

    if c.type == ChatType.PRIVATE:
        ct = "private"

    return ct