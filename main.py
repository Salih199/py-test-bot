import telebot
from telebot import types,util
from googletrans import Translator
BOT_TOKEN = "884799511:AAGLB7w1FPkt-tYOfwCCUFj-wMLC4a4uz1Y"

bot = telebot.TeleBot(BOT_TOKEN)

text_message={
  "welcomes": "welcome! \n This bot is group supporter bot." ,
  "new_members" :
    u"hello {name} \n welcome to this group",
  " byebye": "bye!! \n we will miss you!!!!!!",
  "leave": "this is not my group b yeee",
  "help":"what can i do for you?"
  
  }
commands={
  "translat":["tran","tr","Tr"]
}

@bot.message_handler(commands = ["start"])
def welcome (message):
  bot.send_message(message.chat.id,text_message ["welcomes"])

@bot.chat_member_handler()
def memberhandler(message:types.ChatMemberUpdated):
  newresponse= message.new_chat_member
  if newresponse.status == "member":
    bot.send_message(message.chat.id,text_message["new_members"].format(name= newresponse.user.first_name))
  if newresponse.status == "left":
    bot.send_message(message.chat.id,"byebye")
@bot.my_chat_member_handler()
def leave(message:types.ChatMemberUpdated):
  update= message.new_chat_member
  if update.status == "member":
     bot.send_message(message.chat.id,text_message["leave"])
     bot.leave_chat(message.chat.id)
@bot.message_handler(func=lambda m:True)   
def replys(message):
  word = message.text.split()
  if word[0].lower() in "hilm" :
    bot.reply_to(message,text_message["help"])
  if word[0] in "hello":
    translator=Translator()
    translation=translator.translate(word[1],dest="ar")
    bot.reply_to(message,"translation.text")

bot.infinity_polling(allowed_updates=util.update_types)
