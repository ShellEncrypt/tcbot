import telebot
from random import randint
bot = telebot.TeleBot('1670953127:AAH6N-AJ9E4Rvek7i3cS8u50vigjk6B3oJo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('🔥 Автарка 30₽ 🔥','☄️ Шапка 50₽ ☄️')
keyboard1.row('🎋 Оверлей 40₽ 🎋','🌴 Интро 40₽ 🌴')
keyboard1.row('🐙 Пиар 20₽ 🐙','🍷 Идентификация QIWI 15₽ 🍷')

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Привет 👋! Это бот 🤖 магазин TheCookiss 🍪.\nТут ты можешь себе купить крутые шапки 🌋, аватарки 🔮 и оформления ✉️!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == '🔥 Автарка 30₽ 🔥':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buya')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 30₽', reply_markup=markup)
        elif message.text == '☄️ Шапка 50₽ ☄️':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buys')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 50₽', reply_markup=markup)
        elif message.text == '🎋 Оверлей 40₽ 🎋':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buyo')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 40₽', reply_markup=markup)
        elif message.text == '🌴 Интро 40₽ 🌴':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buyi')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 40₽', reply_markup=markup)
        elif message.text == '🐙 Пиар 20₽ 🐙':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buyp')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 20₽', reply_markup=markup)
        elif message.text == '🍷 Идентификация QIWI 15₽ 🍷':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='buyq')
            markup.add(item1)
            mess = bot.send_message(message.chat.id, '🏦 Сумма: 15₽', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'buya':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='dao')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'buys':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'buyo':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'buyi':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'buyp':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwooooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daooooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'buyq':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoooooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoooooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'qwo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 30₽\nНа QIWI: THECOOKISS\nОставить комментарий: av"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'dao':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 30₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: av"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwoo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 50₽\nНа QIWI: THECOOKISS\nОставить комментарий: sh"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'daoo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 50₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: sh"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 40₽\nНа QIWI: THECOOKISS\nОставить комментарий: ove"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'daooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 40₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: ove"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwoooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 40₽\nНа QIWI: THECOOKISS\nОставить комментарий: in"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'daoooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 40₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: in"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwooooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 20₽\nНа QIWI: THECOOKISS\nОставить комментарий: pr"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'daooooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 20₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: pr"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwoooooo':
                bot.send_message(call.message.chat.id, "ОПЛАТА КИВИ НЕДОСТУПНА")
            if call.data == 'daoooooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 15₽\nНа: https://www.donationalerts.com/r/famii_python\nОставить комментарий: ide"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @fa_mii")

    except:
        print("SOME PROBLEM HAPPENED!")

bot.polling()
