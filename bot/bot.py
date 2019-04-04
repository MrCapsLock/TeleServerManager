#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TELEGRAM SERVER MANAGER BOT !
"""

import logging
import configparser

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ------------------------------------------------------------------------------------------------------
# Configuration
# Enable Logging
# log_location = "logs/bot.log"
from stages import Stages
from user import User

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuring bot
try:
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))
except IOError:
    logger.error("Cant Open The Config File !")
    exit(1)


# ------------------------------------------------------------------------------------------------------
def start(bot: Bot, update: Update, **optional_args):
    usr = User(update.message.from_user)
    if usr.verify :
        msg = "انتخاب کنید:"
        bot.send_message(
            chat_id=update.message.from_user.id,
            text=msg,
            reply_markup=Stages.main_menu()
        )
    else :
        msg = "متاسفانه این بات تنها برای افراد خاص قابل دسترس است."
        bot.send_message(
            chat_id=update.message.from_user.id,
            text=msg,
        )

# ------------------------------------------------------------------------------------------------------
def error(bot, update, error):
    logger.error('Update "%s" caused error "%s"', update, error)


# ------------------------------------------------------------------------------------------------------
def main():
    logger.info("Bot Starts !")
    updater = Updater(config['DEFAULT']['token'])
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start, pass_user_data=True, pass_chat_data=True))

    # Messages
    updater.dispatcher.add_handler(MessageHandler(Filters.text, start, pass_user_data=True, pass_chat_data=True))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


# ------------------------------------------------------------------------------------------------------
if __name__ == "__main__": main()
