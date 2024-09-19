import telebot
from telebot import types

API_TOKEN = '7436934192:AAHjqzxBMjk0t6Y8ZFsQBJ8rusldrLdDQ8A'
QUESTIONS_CHAT_ID = "-4500298835"
REVIEWS_CHAT_ID = "-4515789567"

bot = telebot.TeleBot(API_TOKEN)

user_states = {}

qustion_button = "Задать вопрос"
review_button = "Оставить отзыв"


start_text = """Я бот подкаста «Что-то на окейном». 

Я создан специально для того, чтобы вы могли написать свой вопрос или отзыв после прослушивания подкаста. 

Я все передам Саше и Насте."""

bot.remove_webhook()



def create_one_time_keyboard(buttons):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    for button_name in buttons:
        button = types.KeyboardButton(button_name)
        markup.add(button)
    return markup



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = create_one_time_keyboard([qustion_button, review_button])
    bot.send_message(message.chat.id, start_text, reply_markup=markup)
    user_states[message.chat.id] = 'waiting_for_button'




@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_for_button')
def handle_button_press(message):
    if message.text == qustion_button:
        bot.send_message(message.chat.id, "Введите вопрос:")
        user_states[message.chat.id] = 'waiting_for_question'
    elif message.text == review_button:
        bot.send_message(message.chat.id, "Введите отзыв:")
        user_states[message.chat.id] = 'waiting_for_review'
    else:
        bot.send_message(message.chat.id, "Выберите действующую кнопку.")




@bot.message_handler(func=lambda message: user_states.get(message.chat.id) in ['waiting_for_question', 'waiting_for_review'])
def handle_text_input(message):
    user_name = bot.get_chat_member(message.chat.id, message.from_user.id).user.username
    
    if user_states[message.chat.id] == 'waiting_for_question':
        text_to_send = f"Вопрос от пользавателя @{user_name}: \n\n{message.text}"
        bot.send_message(QUESTIONS_CHAT_ID, text_to_send)
        bot.reply_to(message, "Ваш вопрос принят!")
        
    elif user_states[message.chat.id] == 'waiting_for_review':
        text_to_send = f"Отзыв от пользавателя @{user_name}: \n\n{message.text}"
        bot.send_message(REVIEWS_CHAT_ID, text_to_send)
        bot.reply_to(message, "Ваш отзыв принят!")
    
    markup = create_one_time_keyboard([qustion_button, review_button])
    user_states[message.chat.id] = 'waiting_for_button'




bot.polling()