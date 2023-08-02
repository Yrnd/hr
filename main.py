import random
import time
import telebot
from telebot import types
from Class import Message_history, Application


bot = telebot.TeleBot('6597318240:AAGBAAcI3xgovQM7JefszGAymzLhNv9doUQ')

Message = Message_history()
App = Application()
admin_panel = Application()
app_folder = 'folder/app_base.txt'
msg_folder = 'folder/mh_base.txt'


@bot.message_handler(commands=["admin"])
def admin_panel(message):
    if verify_admin(message.from_user.id):
        bot.send_message(message.chat.id, text='Список анкет:')
    else:
        ...

@bot.message_handler(commands=["start"])
def start(message):
    id = message.chat.id
    user_id = message.from_user.id
    App.dict = load_1(App.dict, app_folder)
    Message.history = load_2(Message.history, msg_folder)
    if Check_ID(user_id):
        if App.dict[user_id]["Stage"] == "10":
            answer = 'Политика нашей компании подразумевает сотрудничество с лицами от 16ти лет' \
                     '\nподрастите немного и возвращайтесь обратно)'
            bot.send_message(id, answer)
        elif App.dict[user_id]["Stage"] == "6":
            answer = 'Заявка уже отправлена, ожидайте ответа оператора⏰'
            bot.send_message(id, answer)
        elif App.dict[user_id]["Stage"] != "6":
            answer = 'Вы уже заполняете заявку, завершите начатое'
            bot.send_message(id, answer)
            Recruting(message=message)
        else:
            try:
                App.dict.pop(user_id)
            except:
                ...
            bot.send_message(id, "Ваша заявка не дошла до сервера, "
                                 "проверьте подключение и попробуйте отправить новую")
            pre_talk(id, message.from_user.id)
    else:
        pre_talk(id, message.from_user.id)


def Check_ID(id):
    if App.dict.get(id) is not None:
        return True
    else:
        return False


def pre_talk(id, user_id):
    App.add_key(user_id)
    Message.add_key(user_id)
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton("Начать✅", callback_data='app_ready'))
    answer = 'Мы готовы предложить вам вакансию,\nно для этого необходимо заполнить небольшую анкету '
    bot.send_message(id, answer,reply_markup=markup_inline)
    Message.history[user_id].append('Напишите свой город, район города')


@bot.callback_query_handler(func=lambda call: True)
def Recruting_talk(call):
    if call.data == "app_ready":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Напишите свой город, район города')
    elif call.data == "side_job":
        App.dict[call.message.chat.id]["Employment_type"] = "Подработка"
        Message.history[call.message.chat.id].append('Подработка')
        App.dict[call.message.chat.id]["Stage"] = "2"
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Сколько вам лет?')
        Message.history[call.message.chat.id].append('Сколько вам лет?')
    elif call.data == "ft_job":
        App.dict[call.message.chat.id]["Employment_type"] = "Полная_занятость"
        Message.history[call.message.chat.id].append('Полная_занятость')
        App.dict[call.message.chat.id]["Stage"] = "2"
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Сколько вам лет?')
        Message.history[call.message.chat.id].append('Сколько вам лет?')
    elif call.data == "var_job":
        App.dict[call.message.chat.id]["Employment_type"] = "Свой_вариант"
        Message.history[call.message.chat.id].append('Свой_вариант')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Продолжить", callback_data='continue'))
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Вариант занятости будет обговорен с оператором после заполнения анкеты'
                                   'Для продолжения анкетирования нажмите кнопку', reply_markup=markup)
        App.dict[call.message.chat.id]["Stage"] = "2"
    elif call.data == "continue":
        time.sleep(0.5)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Сколько вам лет?')
        Message.history[call.message.chat.id].append('Сколько вам лет?')
    elif call.data == "самокат":
        App.dict[call.message.chat.id]["Transport"] = "Самокат"
        Message.history[call.message.chat.id].append('Самокат')
        answer = 'И последний вопрос, откуда вы о нас узнали?'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        Message.history[call.message.chat.id].append(answer)
        App.dict[call.message.chat.id]["Stage"] = "4"
    elif call.data == 'велик':
        App.dict[call.message.chat.id]["Transport"] = "Велосипед"
        Message.history[call.message.chat.id].append('Велосипед')
        answer = 'И последний вопрос, откуда вы о нас узнали?'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        Message.history[call.message.chat.id].append(answer)
        App.dict[call.message.chat.id]["Stage"] = "4"
    elif call.data == 'машина':
        App.dict[call.message.chat.id]["Transport"] = "Машина"
        Message.history[call.message.chat.id].append('Машина')
        answer = 'И последний вопрос, откуда вы о нас узнали?'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        Message.history[call.message.chat.id].append(answer)
        App.dict[call.message.chat.id]["Stage"] = "4"
    elif call.data == 'права':
        App.dict[call.message.chat.id]["Transport"] = "Права"
        Message.history[call.message.chat.id].append('Права')
        answer = 'И последний вопрос, откуда вы о нас узнали?'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        Message.history[call.message.chat.id].append(answer)
        App.dict[call.message.chat.id]["Stage"] = "4"
    elif call.data == 'пешеход':
        App.dict[call.message.chat.id]["Transport"] = "Пешеход"
        Message.history[call.message.chat.id].append('Пешеход')
        answer = 'И последний вопрос, откуда вы о нас узнали?'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        Message.history[call.message.chat.id].append(answer)
        App.dict[call.message.chat.id]["Stage"] = "4"
    elif call.data == 'send':
        App.dict[call.message.chat.id]["Stage"] = "6"
        App.instring_save(app_folder)
        Message.instring_save(msg_folder)
        answer = 'Ваше заявление обрабатывается. Ожидайте, с Вами свяжется наш живой оператор'
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer)
        rnd = random.Random()
        time.sleep(rnd.randint(300, 420))
    # Вот тут надо будет разместить цепочку с панчлайнами, прям можно сразу друг за другом------------------------------
        markup = types.InlineKeyboardMarkup() # эта штука создает кнопки для сообщений
        markup.add(
            types.InlineKeyboardButton("Далее", callback_data='next_1') # callback_data - функция, к которой надо
            # приделать сам функционал так же, как будет дальше
        )
        answer = f'{call.from_user.first_name}' + ', ваше заявление принято!' # сам текст
        bot.send_message(chat_id=call.message.chat.id,
                         text=answer,
                         reply_markup=markup) # это само сообщение, чтобы прибить к нему кнопки,
        # надо добавить параметр reply_markup= и название штуки
    # ------------------------------------------------------------------------------------------------------------------
    # Пример обработки нажатия на кнопку--------------------------------------------------------------------------------
    elif call.data == 'next_1':
        # просто меняем прошлое сообщение на новое, добавляя к нему новую кнопку
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Далее", callback_data='next_2')
        )
        answer = 'Текст сообщения.........'  # сам текст
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=answer,
                              reply_markup=markup)
    # ------------------------------------------------------------------------------------------------------------------
    # И так доходишь до сообщения с двумя кнопками "Согласен" или "Не согласен", потом уже сама диалоговая хуйня будет,
    # которая делается точно так же


@bot.message_handler(content_types=["text"])
def Recruting(message):
    if Check_ID(message.from_user.id):
        if App.dict[message.from_user.id]["Stage"] == "10":
            answer = 'Политика нашей компании подразумевает сотрудничество с лицами от 16ти лет' \
                     '\nподрастите немного и возвращайтесь обратно)'
            bot.send_message(message.chat.id, answer)
        elif App.dict[message.from_user.id]["Stage"] == "6":
            answer = 'Заявка уже отправлена, ожидайте ответа оператора⏰'
            bot.send_message(message.chat.id, answer)
    try:
        user_id = message.from_user.id
        # City and Employment_type--------------------------------------------------------------------------------------
        if App.dict[user_id]["Stage"] == "0":
            Message.history[user_id].append(message.text)
            App.dict[user_id]["City"] = message.text
            App.dict[user_id]["Name"] = message.from_user.first_name
            App.dict[user_id]["Stage"] = "1"
        if App.dict[user_id]["Stage"] == "1":
            markup_inline = types.InlineKeyboardMarkup(row_width=1)
            markup_inline.add(
                              types.InlineKeyboardButton("Подработка", callback_data='side_job'),
                              types.InlineKeyboardButton("Полная занятость", callback_data='ft_job'),
                              types.InlineKeyboardButton("Свой вариант", callback_data='var_job')
                              )
            answer = 'Вы рассматриваете подработку или полную занятость ?'
            Message.history[user_id].append(answer)
            bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=markup_inline)

        # --------------------------------------------------------------------------------------------------------------
        # Age and Transport---------------------------------------------------------------------------------------------
        if App.dict[user_id]["Stage"] == "2":
            try:
                int(message.text)
                if int(message.text) < 16:
                    App.dict[user_id]["Stage"] = "10"
                    Message.history[user_id].append(message.text)
                    App.instring_save(app_folder)
                    answer = 'Политика нашей компании подразумевает сотрудничество с лицами от 16ти лет' \
                             '\nподрастите немного и возвращайтесь обратно)'
                    bot.send_message(message.chat.id, answer)
                else:
                    App.dict[user_id]["Age"] = f"{int(message.text)}"
                    App.dict[user_id]["Stage"] = "3"
                    Message.history[user_id].append(f"{int(message.text)}")
                    markup_inline1 = types.InlineKeyboardMarkup(row_width=1)
                    markup_inline1.add(
                        types.InlineKeyboardButton("Самокат", callback_data='самокат'),
                        types.InlineKeyboardButton("Велосипед", callback_data='велик'),
                        types.InlineKeyboardButton("Авто", callback_data='машина'),
                        types.InlineKeyboardButton("Нет авто, но есть права", callback_data='права'),
                        types.InlineKeyboardButton("Я пеший курьер", callback_data='пешеход')
                    )
                    answer = 'Хорошо, теперь о транспорте. Как вы будете осуществлять курьерскую деятельность?'
                    Message.history[message.from_user.id].append(answer)
                    bot.send_message(message.chat.id, answer, reply_markup=markup_inline1)
            except:
                bot.send_message(chat_id=message.chat.id, text='Введите возраст в правильном формате, цифрами блять')
        # --------------------------------------------------------------------------------------------------------------
        # How Know About Us---------------------------------------------------------------------------------------------
        if App.dict[user_id]["Stage"] == "4":
            App.dict[user_id]["Stage"] = "5"
            App.dict[user_id]["Referral"] = message.text
            Message.history[user_id].append(message.text)
            markup_inline2 = types.InlineKeyboardMarkup()
            markup_inline2.add(types.InlineKeyboardButton("Отправить", callback_data='send'))
            bot.send_message(message.chat.id, 'Анкета заполнена, нажмите отправить для отправки📩',
                             reply_markup=markup_inline2)
        # --------------------------------------------------------------------------------------------------------------
    except Exception as ex:
        print(ex)


def app_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="Сортировка", callback_data="sort_apps"))

def verify_admin(user_id):
    with open('folder/admins') as admins:
        for i in admins.readlines():
            if user_id == int(i):
                return True
        return False


def replace_all(inp):
    chars = ["{", "}", ":", "'", ",", "\n", "[", "]"]
    for i in chars:
        inp = inp.replace(i, "")
    inp = inp.split("конец")
    return inp


def save(string, file):
    with open(file, 'a') as file:
        file.write(f"\n{string}")


def load_1(dict, file_d):
    with open(file_d, 'r') as file:
        for app in file.readlines():
            if app == "":
                continue
            app = replace_all(app)
            app = ''.join(app)
            app = app.split(" ")
            if app.__len__() == 15:
                dict[int(app[0])] = {
                    f"{app[1]}" : f"{app[2]}",
                    f"{app[3]}": f"{app[4]}",
                    f"{app[5]}": f"{app[6]}",
                    f"{app[7]}": f"{app[8]}",
                    f"{app[9]}": f"{app[10]}",
                    f"{app[11]}": f"{app[12]}",
                    f"{app[13]}": f"{app[14]}"
                }
        file.close()
    with open(file_d, 'w') as file:
        file.write("")
    return dict


def load_2(dict, file_d):
    with open(file_d, 'r') as file:
        for app in file.readlines():
            app = replace_all(app)
            app = ''.join(app)
            app = app.split(" ")
            if app.__len__() > 1:
                dict[int(app[0])] = list()
                for i in app[1:]:
                    dict[int(app[0])].append(i)
        file.close()
    with open(file_d, 'w') as file:
         file.write("")
    return dict


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as ex:
        print(ex)
    finally:
        App.instring_save(app_folder)
        Message.instring_save(msg_folder)