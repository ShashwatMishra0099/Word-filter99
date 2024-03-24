# Word-filter99
import telebot

# Replace 'YOUR_ACTUAL_TOKEN' with your Telegram bot token
TOKEN = '7110027433:AAGsM3zFlvER09jVq2ACTKYCfghoqAMZs_s'

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# List of filtered words
filtered_words = ["bad", "inappropriate", "spam", "fuck u"]

@bot.message_handler(func=lambda message: True)
def filter_message(message):
    for word in filtered_words:
        if word in message.text.lower():
            # Delete the message that contains filtered words
            bot.delete_message(message.chat.id, message.message_id)
            # Inform the user about the filtered word
            bot.reply_to(message, "Your message contains a filtered word and has been deleted.")
            break

# Start the bot
bot.polling()
