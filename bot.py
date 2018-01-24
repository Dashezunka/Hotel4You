import logging

from telegram import Location
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler, RegexHandler

import config
import keyboards

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start_greeting(bot, update, chat_data):
    chat_data.clear()
    update.message.reply_text('Привет! Я помогу тебе быстро подобрать отличный отель с помощью сервиса booking.com.', reply_markup=keyboards.REMOVE_KB)
    update.message.reply_text('Если ты готов - просто напиши мне любое сообщение')

def start_description(bot, update, chat_data):
    bot.send_message(update.message.chat_id, text='Рад твоему сообщению!')
    bot.send_message(update.message.chat_id, text='Как я уже говорил, я использую сервис booking.com, как наиболее надежный и удобный сервис.')
    bot.send_message(update.message.chat_id, text='Все бронирования ты будешь делать на booking.com самостоятельно, а я отберу для тебя отели согласно твоим личным предпочтениям.')
    bot.send_message(update.message.chat_id, text='Если ты не останавливаешься в хостелах – ты больше не увидишь их в своем списке отелей, но, если захочешь, я буду показывать тебе только хостелы.')
    bot.send_message(update.message.chat_id, text='Я не буду просить дополнительную комиссию, все цены – согласно ценам на booking.com, обязательно проверь!')
    bot.send_message(update.message.chat_id, text='Чтобы подобрать лучшие варианты, мне нужно задать тебе несколько вопросов. Давай попробуем?)',
                     reply_markup=keyboards.YES_NO_KB)

def type_of_hotel(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Отлично! Где ты предпочитаешь останавливаться? Выбери один из возможных вариантов ниже:',
                          reply_markup=keyboards.TYPE_HOTEL_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def back_to_the_main(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Хорошо! Обращайся в любое время!',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    bot.send_message(query.message.chat_id,
                     text='Нажми на кнопку снизу, как только снова захочешь начать общение с ботом',
                     reply_markup=keyboards.START_KB)


if __name__ == '__main__':
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_greeting, pass_chat_data=True))
    dispatcher.add_handler(MessageHandler(Filters.text, start_description, pass_chat_data=True))
    dispatcher.add_handler(CallbackQueryHandler(type_of_hotel, pattern='type_of_hotel'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_the_main, pattern='back_to_main'))

    updater.start_polling()
    updater.idle()
