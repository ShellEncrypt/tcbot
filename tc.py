import telebot
import urllib
from random import randint

bot = telebot.TeleBot('1670953127:AAH6N-AJ9E4Rvek7i3cS8u50vigjk6B3oJo')

keyboardm = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardm.row('🛒 Товары 🛒')
keyboardm.row('🔴 Канал 🔴','🔰 Лучшая группа вк по дизайну 🔰')
keyboardm.row('🔵 Дискорд канал 🔵','💬 Коментарии 💬')


keyboardaa = telebot.types.InlineKeyboardMarkup(row_width=1)
avat=telebot.types.InlineKeyboardButton('🔥 Автарка 30₽ 🔥', callback_data='avat')
shap=telebot.types.InlineKeyboardButton('☄️ Шапка 50₽ ☄️', callback_data='shap')
ower=telebot.types.InlineKeyboardButton('🎋 Оверлей 40₽ 🎋', callback_data='ower')
into=telebot.types.InlineKeyboardButton('🌴 Интро 40₽ 🌴', callback_data='into')
pier=telebot.types.InlineKeyboardButton('🐙 Пиар 20₽ 🐙', callback_data='pier')
prew=telebot.types.InlineKeyboardButton('🦋 Превю 15₽ 🦋', callback_data='prew')
iden=telebot.types.InlineKeyboardButton('🍷 Идентификация QIWI 15₽ 🍷', callback_data='iden')
keyboardaa.add(avat, shap, ower, into, pier, prew, iden)

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Привет 👋! Это бот 🤖 магазин TheCookiss 🍪.\nТут ты можешь себе купить крутые шапки 🌋, аватарки 🔮 и оформления ✉️!', reply_markup=keyboardm)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == '🛒 Товары 🛒':
            bot.send_message(message.chat.id, "👇 Товары доступны в клавиатуре 👇", reply_markup=keyboardaa)
        if message.text == '🔴 Канал 🔴':
            bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCnWTKtFn9pb4-M0CxW24nWQ")
        if message.text == '🔰 Лучшая группа вк по дизайну 🔰':
            bot.send_message(message.chat.id, "https://vk.com/club201578413​​")
        if message.text == '🔵 Дискорд канал 🔵':
            bot.send_message(message.chat.id, "https://discord.gg/Dxpd8D6Xd8")
        if message.text == '💬 Коментарии 💬':
            bot.send_message(message.chat.id, "@thecookisscom")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            avatar='https://github.com/FAMII/tcbphotos/blob/main/avatar.jpg?raw=true'
            ava = open('avatar.jpg','wb')
            ava.write(urllib.request.urlopen(avatar).read())
            ava.close()
            
            shapka='https://github.com/FAMII/tcbphotos/blob/main/shapka.jpg?raw=true'
            sh = open('shapka.jpg','wb')
            sh.write(urllib.request.urlopen(shapka).read())
            sh.close()
            shapka2='https://github.com/FAMII/tcbphotos/blob/main/shapka2.jpg?raw=true'
            sh2 = open('shapka2.jpg','wb')
            sh2.write(urllib.request.urlopen(shapka2).read())
            sh2.close()
            
            owerlay='https://github.com/FAMII/tcbphotos/blob/main/owerlay.png?raw=true'
            owr = open('owerlay.png','wb')
            owr.write(urllib.request.urlopen(owerlay).read())
            owr.close()
            
            intro='https://github.com/FAMII/tcbphotos/blob/main/intro.mp4?raw=true'
            intr = open('intro.mp4','wb')
            intr.write(urllib.request.urlopen(intro).read())
            intr.close()
            if call.data == 'avat':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='avab')
                markup.add(item1)
                img = open('avatar.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img,  """
Описание для аватарки 🏔
После покупки данного товара Вы получите топовую 🔥 аватарку для вашего ютуб канала

Сроки:
Заказ🌭 выполняется максимум за 3 рабочих дня🥠

План описания:⚡️
1) Ник🍔
2) Стиль🦑
Стили:
Гейм🎮
Спелл🔮
Вкусный🍬
Орео🍪
Фарчок🍧
Рофл🦀
""", reply_markup=markup)
            if call.data == 'shap':
                bot.send_chat_action(call.message.chat.id, 'upload_photo')
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='shapb')
                markup.add(item1)
                img = open('shapka2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, caption="""
🏦 Сумма: 50₽

После покупки🔖 данного товара😎 Вы получите🍩 топовую шапку🛸 для вашего YouTube🍿 канала 

Сроки:
Заказ выполняется максимум за 1-3 рабочих дня🥠

План описания:🍦
1) Ваша название канала🦐
2) Тематика канала🥙
""", reply_markup=markup)
            if call.data == 'ower':
                bot.send_chat_action(call.message.chat.id, 'upload_photo')
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='owerb')
                markup.add(item1)
                img = open('shapka2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, """
Описание оверлея
После покупки🔖 данного товара Вы получите топовый🔥 оверлей для вашего💈 YouTube👽  канала

Сроки:
Заказ выполняется максимум за 1-2 недели🥠

План описания:🌭
1) Ваше название канала👾
2) Тематика канала🎉                
""", reply_markup=markup)
            if call.data == 'into':
                bot.send_chat_action(call.message.chat.id, 'upload_video')
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='intob')
                markup.add(item1)
                img = open('intro.mp4', 'rb')
                bot.send_video(call.message.chat.id, img, caption="""
Описание для интро🎬
После покупки данного товара Вы получите топовое🔥 интро для вашего ютуб канала

Сроки:
Заказ🌭 выполняется максимум за 3 рабочих дня🥠

План описания:⚡️
1) Ник🍔
2) Стиль🦑
Стили:
Гейм🎮
Спелл🔮
Вкусный🍬
Орео🍪
Фарчок🍧
Рофл🦀
""", reply_markup=markup)
            if call.data == 'pier':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='pierb')
                markup.add(item1)
                bot.send_message(call.message.chat.id, """
Описание для пиара 🎨
После покупки вас прорекламируют на канале TheCookiss 🏕
https://www.youtube.com/channel/UCnWTKtFn9pb4-M0CxW24nWQ
""", reply_markup=markup)
            if call.data == 'prew':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='prewb')
                markup.add(item1)
                bot.send_message(call.message.chat.id, """
Описание для превью🥙
После покупки данного товара Вы получите топовое🍿 превью для вашего
видео🦐

Сроки:
Заказ😎 выполняется максимум за 3 рабочих дня🥠

План описания:⚡️
1) Тема видео🚀
2) Текст на превью🛰
""", reply_markup=markup)
            if call.data == 'iden':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton("🔑 Купить 🔑", callback_data='idenb')
                markup.add(item1)
                bot.send_message(call.message.chat.id, """
📗 Сумма: 15₽
""", reply_markup=markup)
            if call.data == 'avab':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='dao')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'shapb':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'owerb':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'intob':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'pierb':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwooooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daooooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'prewb':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwoooooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daoooooo')
                sop.add(qiwi,donal)
                bot.send_message(call.message.chat.id, "⚡️ Выберите способ оплаты:", reply_markup=sop)
            if call.data == 'idenb':
                sop = telebot.types.InlineKeyboardMarkup(row_width=2)
                qiwi = telebot.types.InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qwooooooo')
                donal = telebot.types.InlineKeyboardButton("🍀 DonationAlerts 🍀", callback_data='daooooooo')
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
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 50₽\nНа QIWI: THECOOKISS\nОставить комментарий: tpp"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'daoooooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 50₽\nНа: https://www.donationalerts.com/r/thecookiss\nОставить комментарий: tpp"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @thecookissoriginal")
            if call.data == 'qwooooooo':
                bot.send_message(call.message.chat.id, "ОПЛАТА КИВИ НЕДОСТУПНА")
            if call.data == 'daooooooo':
                bot.send_message(call.message.chat.id, "💸 Сумма к оплате: 15₽\nНа: https://www.donationalerts.com/r/famii_python\nОставить комментарий: ide"+str(randint(1, 999999999))+"\n\nПосле оплаты написать коментарий в @fa_mii")

    except:
        print("SOME PROBLEM HAPPENED!")

bot.polling()
