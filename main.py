import telebot
BOT_TOKEN = "884799511:AAGLB7w1FPkt-tYOfwCCUFj-wMLC4a4uz1Y"

bot = telebot.TeleBot(BOT_TOKEN)

text_message={
  "welcomes": "welcome! \n This bot is group supporter bot." ,
  "help":"what can i do for you?"
  }
@bot.message_handler(commands = ["start"])
def welcome (message):
  bot.send_message(message.chat.id,text_message ["welcomes"])
  
@bot.message_handler(func=lambda m:True)   
def replys(message):
  word = message.text.split()
  if word[0].lower() in "hilm" :
    bot.reply_to(message,text_message["help"])

bot.infinity_polling()
