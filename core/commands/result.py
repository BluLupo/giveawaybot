from core import decorators
from core.database.repository.users import UserRepository

@decorators.owner.init
@decorators.private.init
def init(update,context):
    bot = context.bot
    user = UserRepository().getRandom()
    message = "<b>The winner is:</b>\nUser_Id: <code>{}</code>\nNickname: {}".format(user['user_id'],"@"+user['user_nickname'])
    bot.send_message(update.message.chat_id, text=message, parse_mode='HTML')