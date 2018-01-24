from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

REMOVE_KB = ReplyKeyboardRemove()

START_KB = ReplyKeyboardMarkup([[KeyboardButton('/start')]], resize_keyboard=True)

YES_NO_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='type_of_hotel'),
                                  InlineKeyboardButton('Нет', callback_data='back_to_main')]
                                 ])

TYPE_HOTEL_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Отели', callback_data='1'),
                                       InlineKeyboardButton('Минигостиницы', callback_data='2')],
                                      [InlineKeyboardButton('Лоджи', callback_data='3'),
                                       InlineKeyboardButton('Загородные дома', callback_data='4')],
                                      [InlineKeyboardButton('Хостелы', callback_data='5'),
                                       InlineKeyboardButton('Апартаменты', callback_data='6')],
                                      [InlineKeyboardButton('Гостевые дома', callback_data='7'),
                                       InlineKeyboardButton('Ботели', callback_data='8')],
                                      [InlineKeyboardButton('Курортные отели', callback_data='9'),
                                       InlineKeyboardButton('Дома для отпуска', callback_data='10')],
                                      [InlineKeyboardButton('Отели типа R&B', callback_data='11'),
                                       InlineKeyboardButton('Не важно', callback_data='0')],
                                      [InlineKeyboardButton('Назад', callback_data='back_to_main')]
                                      ])