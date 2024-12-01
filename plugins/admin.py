from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from config import *
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully 😁")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("🦋 Select Plan To Upgrade...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("🪙 Basic", callback_data="vip1")],
				   [InlineKeyboardButton("⚡ Standard", callback_data="vip2")],
				   [InlineKeyboardButton("💎 Pro", callback_data="vip3")],
				   [InlineKeyboardButton("✖️ Cancel ✖️",callback_data = "cancel")]
				   
				   ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
	await message.reply_text("😁 Power Cease Mode...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("Limit 1GB", callback_data="cp1")],
				   [InlineKeyboardButton("All Power Cease", callback_data="cp2")],
				   [InlineKeyboardButton("✖️ Cancel ✖️",callback_data = "cancel")]
				   
				   ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"Do You Really Want To Reset Daily Limit To Default Data Limit 2GB ?",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• Yes ! Set As Default •",callback_data = "dft")],
				   [InlineKeyboardButton("❌ Cancel ❌",callback_data = "cancel")]
				   ]))



@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 21474836500
	uploadlimit(int(user_id),21474836500)
	usertype(int(user_id),"🪙 Basic")
	addpre(int(user_id))
	await update.message.edit("Added Successfully To Premium Upload Limit 20 GB")
	await bot.send_message(user_id,"Hey You Are Upgraded To Basic. Check Your Plan Here /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"⚡ Standard")
	addpre(int(user_id))
	await update.message.edit("Added Successfully To Premium Upload Limit 50 GB")
	await bot.send_message(user_id,"Hey You Are Upgraded To Standard. Check Your Plan Here /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot, update):
    try:
        # Check if there is a reply to a message containing the user_id
        if update.message.reply_to_message and "/addpremium" in update.message.reply_to_message.text:
            id = update.message.reply_to_message.text.split("/addpremium")
            user_id = id[1].replace(" ", "")
        else:
            # If no reply message, prompt the owner to input a user_id
            await update.message.edit("Please input the user_id as a reply to this message.")
            return

        # Convert user_id to an integer
        user_id = int(user_id)

        # Define premium limits and upgrade user
        inlimit = 107374182400
        uploadlimit(user_id, inlimit)
        usertype(user_id, "💎 Pro")
        addpre(user_id)

        # Notify both the admin and the user
        await update.message.edit("Added Successfully To Premium Upload Limit 100 GB")
        await bot.send_message(user_id, "Hey! You are upgraded to Pro. Check your plan here: /myplan")

    except ValueError:
        await update.message.edit("Invalid user_id. Please provide a valid numeric user_id.")
    except Exception as e:
        await update.message.edit(f"An error occurred: {e}")



@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 2147483652
	uploadlimit(int(user_id), 2147483652)
	usertype(int(user_id),"⚠️ Account Downgraded")
	addpre(int(user_id))
	await update.message.edit("Added Successfully To Upload Limit 2GB")
	await bot.send_message(user_id,"Hey You Are Downgraded To Cease Limit 2GB. Check Your Plan Here /myplan \n\n**Contact Admin :** @calladminrobot")


@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 0
	uploadlimit(int(user_id), 0)
	usertype(int(user_id),"⚠️ Account Downgraded")
	addpre(int(user_id))
	await update.message.edit("Added Successfully To Upload Limit 0GB")
	await bot.send_message(user_id,"Hey You Are Downgraded To Cease Limit 0GB. Check Your Plan Here /myplan \n\n**Contact Admin :** @Kirodewal")



@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 2147483652
	uploadlimit(int(user_id), 2147483652)
	usertype(int(user_id),"🆓 Free")
	addpre(int(user_id))
	await update.message.edit("**Daily Data Limit Has Been Reset Successfully.**\n\nThis Account Has Default 2GB Remaining Capacity")
	await bot.send_message(user_id,"**Your Daily Data Limit Has Been Reset Successfully.**\n\nCheck Your Plan Here /myplan\n\n**Contact Admin :** <a href='https://t.me/Kirodewal'>Kirodewal</a>")




