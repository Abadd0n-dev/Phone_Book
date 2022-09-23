import telebot
import phonebookPython as phonebook
import delete_contact as delete
import search_contact as search
import enter_contact as enter

name = ''
surname = ''
phonenumber = 0
user_choice = 0
filtered_list = []
user_for_commands = []
new_data = ''

TOKEN = '5723290877:AAEJCwnb99AdKKiF3gE7f3vcIxK8ZQfwJd0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.ReplyKeyboardMarkup(resize_keyboard=True)
    read_phone_book = telebot.KeyboardButton('Display guide on screen')
    find_contact = telebot.KeyboardButton('Find a contact')
    add_contact = telebot.KeyboardButton('Add contact')
    delete_contact = telebot.KeyboardButton('Delete contact')

    markup.add(read_phone_book, find_contact, add_contact, delete_contact)

    bot.send_message(message.chat.id, 'Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Display guide on screen':
            if len(phonebook.menu()) == 0:
                bot.send_message(message.from_user.id, f'The phone book is empty.')
            count = 0
            for i, j in sorted(phonebook.menu().items()):
                count += 1
                bot.send_message(message.from_user.id,f'{count}. {i} {j}')
        elif message.text == 'Add contact':
            bot.send_message(message.from_user.id, 'Enter your name: ')
            bot.register_next_step_handler(message, get_name)
        elif message.text == 'Add contact':
            bot.send_message(message.from_user.id, 'Enter the name/phone number of the contact you want to search for: ')
            bot.register_next_step_handler(message, find_contact_bot)
        elif message.text == 'Delete contact':
            bot.send_message(message.from_user.id, 'Enter the name/phone number of the contact you want to delete: ')
            bot.register_next_step_handler(message, deleteC)

#def get_name():

#def find_contact_bot():

#def deleteC():

bot.polling(none_stop=True)