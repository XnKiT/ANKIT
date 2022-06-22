import os

from telethon import Button, events

from Ankit import *

IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/c9d2beabc2870756c2df8.mp4"
)
ms = 27

ALIVE = os.environ.get(
    "ALIVE", "@XnKiTKuMaR"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@Ankit.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ AbOuT Me ⚜", "https://xnkit.github.io/k/")]]
    await Ankit.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
