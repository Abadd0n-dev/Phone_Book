import telebot
import get_contact as contact
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
            if  len(contact.file_contents) == 0:
                bot.send_message(message.from_user.id, f'The phone book is empty.')
            count = 0
            for i, j in sorted(contact.file_contents.items()):
                count += 1
                bot.send_message(message.from_user.id,f'{count}. {i} {j}')
        elif message.text == 'Add contact':
            bot.send_message(message.from_user.id, 'Enter your name: ')
            bot.register_next_step_handler(message, get_name)
        elif message.text == 'Search contact':
            bot.send_message(message.from_user.id, 'Enter the name/phone number of the contact you want to search for: ')
            bot.register_next_step_handler(message, find_contact_bot)
        elif message.text == 'Delete contact':
            bot.send_message(message.from_user.id, 'Enter the name/phone number of the contact you want to delete: ')
            bot.register_next_step_handler(message, deleteC)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Enter last name: ')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Enter phone number: ')
    bot.register_next_step_handler(message, get_phonenumber)

def get_phonenumber(message):
    global phonenumber
    phonenumber = message.text
    keyboard = telebot.InlineKeyboardMarkup()
    yes = telebot.InlineKeyboardButton(text='Yes', callback_data='yes')
    keyboard.add(yes)
    no = telebot.InlineKeyboardButton(text='No', callback_data='no')
    keyboard.add(no)

    question = f'Last name and first name: {name} {surname}, telephone {str(phonenumber)}. Is that right? '
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def find_contact_bot(message):
    global filtered_list
    count = 0
    for name, phone in contact.file_contents.items():
        if (message.text.lower() in name.lower()) or (message.text.lower() in phone.lower()):
            filtered_list.append(f'{name},{phone}')
            count += 1
            filtered_list.append(f'{name},{phone}')
            bot.send_message(message.from_user.id, f'{count}. {name}, {phone}')
            filtered_list.clear()
    if count == 0:
        bot.send_message(message.from_user.id, f'Contact not found.')

def null_data(message):
    if len(contact.file_contents) == 0:
        bot.send_message(message.from_user.id, f'Contact not found.')

def get_userchoice(message, filtered_list):
    global user_choice
    global user_for_commands
    user_choice = int(message.text)
    user_for_commands = filtered_list[user_choice - 1].split(',')
    delete.deleteContact(user_for_commands[1])
    bot.send_message(message.from_user.id, f'Removed contact: {filtered_list[user_choice - 1]}')
    filtered_list.clear()

def deleteC(message):
    global filtered_list
    count = 0
    null_data(message)
    for name, phone in contact.file_contents.copy().items():
        if (message.text.lower() in name.lower()) or (message.text.lower() in phone.lower()):
            filtered_list.append(f'{name},{phone}')
            count += 1
            bot.send_message(message.from_user.id, f'{count}. {name}, {phone}')
    if len(filtered_list) > 1:
        bot.send_message(message.from_user.id, f'¬ыберите контакт дл€ удалени€ по его номеру в списке: ')
        bot.register_next_step_handler(message, get_userchoice, filtered_list)
    elif len(filtered_list) == 1:
        user_for_commands = filtered_list[0].split(',')
        delete.deleteContact(user_for_commands[1])
        bot.send_message(message.from_user.id, f'Removed contact: {filtered_list[0]}')
        filtered_list.clear()
    else:
        bot.send_message(message.from_user.id, 'Contact not found.')

bot.polling(none_stop=True)