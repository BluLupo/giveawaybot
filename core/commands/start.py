from core import decorators
from core.utilities.menu import build_menu
from core.database.repository.get_config import ConfRepository
from core.database.repository.users import UserRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.private.init
def init(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    list_buttons = []
    confs = ConfRepository().getAll()
    for conf in confs:
        if conf['switch'] == 1:
            list_buttons.append(InlineKeyboardButton(text=conf['button_text'], callback_data='save_user'))
            menu = build_menu(list_buttons,2)
            msg = conf['main_text']
            bot.send_message(chat,msg,reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")

def save_user(update, context):
    query = update.callback_query
    get_user = update.effective_user
    userdb = UserRepository().getById(get_user.id)
    if get_user.username is not None:
        if userdb:
            query.edit_message_text("You have already participated in the giveaway!",parse_mode='HTML')
        else:
            u_username = get_user.username
            data = [(get_user.id,u_username)]
            UserRepository().add(data)
            query.edit_message_text("Thanks for taking part in the giveaway!",parse_mode='HTML')
    else:
        query.edit_message_text("You cannot participate if you don't have a username set!\nTo try again press /start",parse_mode='HTML')