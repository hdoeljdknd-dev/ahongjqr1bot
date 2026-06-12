import telebot

# BotFather ကပေးတဲ့ Token ကို ဒီမှာ အစားထိုးထည့်ပါ
Done! Congratulations on your new bot. You will find it at t.me/ahongjqr1bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
8878532181:AAG6St4CxxS7VdLWvQx_6HvDFFiw06_bLsA
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ! ကျွန်တော်က သီချင်းရှာပေးမယ့် Bot ဖြစ်ပါတယ်။")

# သီချင်းရှာဖွေမည့် Command (နမူနာစာသားပြန်ပို့ပေးမည့်စနစ်)
@bot.message_handler(func=lambda message: True)
def search_music(message):
    song_name = message.text
    bot.reply_to(message, f"'{song_name}' သီချင်းကို ရှာဖွေနေပါတယ်... (Server ချိတ်ဆက်ရန် လိုအပ်ပါသည်)")

bot.infinity_polling()
