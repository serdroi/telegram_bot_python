import telebot;
bot = telebot.TeleBot('%token%');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  @bot.message_handler(content_types=['text', 'document', 'audio'])
