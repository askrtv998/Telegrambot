import os
import telebot
from telebot import types

TOKEN = '9266889892:AAGEmlqWDRHHLrM1hnw1abC7JiLzGioGDTo'
bot = telebot.TeleBot(TOKEN)

# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    # কন্টাক্ট শেয়ার করার বাটন তৈরি
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_button = types.KeyboardButton(text="📱 আমার ফোন নম্বর শেয়ার করুন", request_contact=True)
    markup.add(contact_button)
    
    bot.send_message(
        message.chat.id, 
        f"স্বাগতম, {user_name}!\n\nআপনার নাম ও ফোন নম্বর দেখতে নিচের বাটনে ক্লিক করে আপনার কন্টাক্ট শেয়ার করুন:", 
        reply_markup=markup
    )

# কন্টাক্ট (ফোন নম্বর) রিসিভ করার হ্যান্ডলার
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_name = message.from_user.first_name
    phone_number = message.contact.phone_number
    
    # কিবোর্ড রিমুভ করার জন্য
    markup = types.ReplyKeyboardRemove()
    
    bot.send_message(
        message.chat.id, 
        f"ধন্যবাদ, {user_name}!\n\nআপনার তথ্য সফলভাবে পাওয়া গেছে:\n👤 নাম: {user_name}\n📱 ফোন নম্বর: +{phone_number}",
        reply_markup=markup
    )

# বট রান করা (Polling মেথড - কোনো হোস্টিং ফায়ারওয়াল ব্লক করবে না)
print("Bot is running...")
bot.infinity_polling()

