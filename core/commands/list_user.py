from core import decorators
from core.database.repository.users import UserRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_menu(buttons, n_cols, header_buttons=False, footer_buttons=False):
  menu=[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

@decorators.owner.init
@decorators.private.init
def init(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    list_buttons = []
    users = UserRepository().getAll()
    for user in users:
        get_url = 'https://t.me/{0}'.format(user['user_nickname'])
        list_buttons.append(InlineKeyboardButton(text="@"+user['user_nickname'], url=get_url))
    menu = build_menu(list_buttons,2)
    msg = "List Participants:"
    bot.send_message(chat,msg,reply_markup=InlineKeyboardMarkup(menu), parse_mode="HTML")