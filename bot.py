import logging

from telegram import Location
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler, RegexHandler

import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update, chat_data):
    chat_data.clear()
    update.message.reply_text('Привет! Я помогу тебе быстро подобрать отличный отель с помощью сервиса booking.com.')
    update.message.reply_text('Если ты готов - просто напиши мне любое сообщение')

def start_finding(bot, update, chat_data):
    bot.send_message(update.message.chat_id, text='Рад твоему сообщению!')
    bot.send_message(update.message.chat_id, text='Как я уже говорил, я использую сервис booking.com, как наиболее надежный и удобный сервис.')
    bot.send_message(update.message.chat_id, text='Все бронирования ты будешь делать на booking.com самостоятельно, а я отберу для тебя отели согласно твоим личным предпочтениям.')
    bot.send_message(update.message.chat_id, text='Если ты не останавливаешься в хостелах – ты больше не увидишь их в своем списке отелей, но, если захочешь, я буду показывать тебе только хостелы.')
    bot.send_message(update.message.chat_id, text='Я не буду просить дополнительную комиссию, все цены – согласно ценам на booking.com, обязательно проверь!')
    bot.send_message(update.message.chat_id, text='Чтобы подобрать лучшие варианты, мне нужно задать тебе несколько вопросов. Давай попробуем?)')

if __name__ == '__main__':
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start, pass_chat_data=True))
    dispatcher.add_handler(MessageHandler(Filters.text, start_finding, pass_chat_data=True))

    updater.start_polling()
    updater.idle()
