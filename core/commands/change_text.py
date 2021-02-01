from core import decorators
from core.database.repository.get_config import ConfRepository

@decorators.owner.init
@decorators.private.init
def update_main_text(update,context):
    bot = context.bot
    message = str(update.message.text[8:]).strip()
    if message != "":
        ConfRepository().setMain([message])
        bot.send_message(update.message.chat_id, text="You succesfully inserted the main text")
    else:
        bot.send_message(update.message.chat_id, text="You can't insert an empty message!")

@decorators.owner.init
@decorators.private.init
def update_button_text(update,context):
    bot = context.bot
    message = str(update.message.text[10:]).strip()
    if message != "":
        ConfRepository().setButton([message])
        bot.send_message(update.message.chat_id, text="You succesfully inserted the button text")
    else:
        bot.send_message(update.message.chat_id, text="You can't insert an empty message!")