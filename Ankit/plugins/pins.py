from telethon import events, Button, types
from Ankit import Ankit
from Ankit.status import *

PINS_TEXT = """
**✘ All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!**

‣ `?pin` - To pinned a reply msg.
‣ `?unpin` - To Unpin the latest pinned msg.
‣ `?unpinall` - To unpinall all pinned msgs at once.
‣ `?pinned` - To get current pinned msg.

**➥Note:** __Add `notify` after ?pin to notify all chat members.__
"""

@Ankit.on(events.NewMessage(pattern="^[?!/]pinned"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await Ankit.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@Ankit.on(events.NewMessage(pattern="^[!?/]pin ?(.*)"))
@is_admin
async def pin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to pin it!")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await Ankit.pin_message(event.chat_id, msg, notify=True)
       return
    await Ankit.pin_message(event.chat_id, msg)   

@Ankit.on(events.NewMessage(pattern="^[!?/]unpin ?(.*)"))
@is_admin
async def unpin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await Ankit.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await Stark.unpin_message(event.chat_id, ok)
    await event.reply(f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.", link_preview=False)

@Ankit.on(events.NewMessage(pattern="^[!?/]permapin"))
@is_admin
async def permapin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to permapin it.")
       return
    hn = await Ankit.send_message(event.chat_id, msg.message)
    await Ankit.pin_message(event.chat_id, hn, notify=True)


@Ankit.on(events.NewMessage(pattern="^[!?/]unpinall"))
async def unpinall(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs!")
       return
    UNPINALL = """
Are you sure you want to 
unpin all msgs?
This action can't be undone!
"""

    await Ankit.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("Confirm", data="unpin")], 
    [Button.inline("Cancel", data="cancel")]])

@Ankit.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await Ankit.unpin_message(event.chat_id)
        await event.edit("Unpinned All Msgs!")
        return 

    await event.answer("Group Creator Required!")

@Ankit.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("Unpinning of all msgs has been cancelled!")
        return 

    await event.answer("Group Creator Required!")


@Ankit.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])
