#!/usr/bin/env python
# -*- coding: utf-8 -*-

### IMPORT ###
import logging
from core import commands
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dsp = updater.dispatcher

    function = dsp.add_handler
    function(CommandHandler('start', commands.start.init))
    function(CommandHandler('list', commands.list_user.init))
    function(CommandHandler('result', commands.result.init))
    function(CommandHandler('setmain', commands.change_text.update_main_text))
    function(CommandHandler('setbutton', commands.change_text.update_button_text))
    function(CommandHandler('config', commands.config.init))
    function(CallbackQueryHandler(commands.start.save_user, pattern='save_user'))
    function(CallbackQueryHandler(commands.config.update_settings))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()