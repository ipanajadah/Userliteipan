from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<u><b>👋🏻 Halooo </b></u><a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>
<blockquote><b>• ᴘʏᴛʜᴏɴ: 3.10.12</b>
<b>• ᴘʏʀᴏɢᴀᴍ: 3.0.2</b>
<b>• ᴛᴏᴛᴀʟ ᴘᴇɴɢɢᴜɴᴀ: {len(ubot._ubot)} users</b>

<u><b>📖 penjelasan menu button:</b></u>
<b>﻿• help menu: untuk melihat menu bot.</b>
<b>• buat userbot: untuk membuat ubot.</b>
<b>• beli userbot: untuk membeli akses.</b>
<b>• support: untuk chat owner jika limit.</b>
<b>• group support: jika ingin bertanya.</b></blockquote>
<u><b>☁ silahkan pilih tombol dibawah ini:</b></u>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
<b>├ Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ </b>
<b>├ 𝙶𝙾𝙿𝙰𝚈 𝟶𝟾𝟻𝟽𝟻𝟶𝟷𝟶𝟽𝟻𝟶𝟻
<b>├ 𝙳𝚊𝚗𝚊 𝟶𝟾𝟻𝟽𝟻𝟶𝟷𝟶𝟽𝟻𝟶𝟻
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

OWNER BOT : <a href=tg://openmessage?user_id={OWNER_ID}>@IPAN9Q</a> 

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢 ᴛʜʀᴇᴇʙᴏᴛ ᴋᴇ </b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├〢 ᴀᴄᴄᴏᴜɴᴛ </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰〢ᴜsᴇʀ ɪᴅ </b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """ <blockquote><b>ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ  <a href=tg://openmessage?user_id={OWNER_ID}>@MAKLUUU</a></b></blockquote>
"""
