##كل سنه و انت طيب 
## كود بيسط كده 


##اتاكد من تنصيب المكاتب
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

#الكود
@Client.on_message(command(["انا مين", "مين انت"]) & filters.group & ~filters.edited)
async def eelkeatib(client: Client, message: Message):
    await message.reply_text(
        f"""💘 ¦ انت روحي » """, 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 .╡", url=f"https://t.me/ch_world_music"),
                ]
            ]
        ),
    )

# كده الكود تم و هيشغل معك
#لو وجهت مشكله تع هنا 
#معرفي @Mk_74_UU
# قناتي 1>>  @MusicElkeatib
# قناتي 1>>  @M_Python_1

#كل سنه و انت طيب💓
 