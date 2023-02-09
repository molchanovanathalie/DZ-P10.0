import telebot

from telebot import types




bot = telebot.TeleBot('6120515342:AAHQvhPENdmBtP5mEV49XXiK3PTXQsC2Ky0')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-проводник в мире ароматов!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Отзывы')
        btn2 = types.KeyboardButton('Как со мной связаться')
        btn3 = types.KeyboardButton('Ассортимент')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)


    elif message.text == 'Отзывы':
        bot.send_message(message.from_user.id, 'Перейдите по ссылке на сайт Авито. Все отзывы представлены там ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    elif message.text == 'Как со мной связаться':
        bot.send_message(message.from_user.id, 'Контакты вы можете найти на сайте Авито ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    if message.text == 'Ассортимент':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Amouage Sunshine')
        btn5 = types.KeyboardButton('M-A Barrois Ganymede')
        btn6 = types.KeyboardButton('Memo Kedu')
        markup.add(btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас аромат', reply_markup=markup)



    if message.text == 'Amouage Sunshine':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('2 ml')
        btn5 = types.KeyboardButton('5 ml')
        btn6 = types.KeyboardButton('10 ml')
        btn7 = types.KeyboardButton('передумал')
        btn8 = types.KeyboardButton('посчитать')
        markup.add(btn4, btn5, btn6, btn7, btn8 )
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас объем', reply_markup=markup)

    sum1 = 0
    sum2 = 0
    sum3 = 0

    def rez(a, b, c):
        return a + b + c

    def handle_message(message):
        if message.text == '2 ml':
            global sum1
            sum1 = 500
            bot.send_message(message.from_user.id, '+ 2 ml')

        if message.text == '5 ml':
            global sum2
            sum2 = 990
            bot.send_message(message.from_user.id, '+ 5 ml')

        if message.text == '10 ml':
            global sum3
            sum3 = 1050
            bot.send_message(message.from_user.id, '+ 10 ml')

        if message.text == 'передумал':
            pass
        if message.text == 'посчитать':
            total_sum = rez(sum1, sum2, sum3)
            bot.send_message(message.from_user.id, 'стоимость заказа ' + str(total_sum) + ' руб', parse_mode='Markdown')





bot.polling(none_stop=True, interval=0)


