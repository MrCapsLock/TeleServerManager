#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TELEGRAM SERVER MANAGER BOT !

License goes here !...
"""

import logging
import configparser
from telegram.ext import Updater, CommandHandler

# ------------------------------------------------------------------------------------------------------
# Configuration
# Enable Logging
log_location = "logs/bot.log"
logging.basicConfig(filename=log_location, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Configuring bot
try:
    config = configparser.ConfigParser()
    config.read_file(open('../config.ini'))
except IOError:
    logger.error("Cant Open The Config File !")
    exit(1)


# ------------------------------------------------------------------------------------------------------
def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hello dear")


# ------------------------------------------------------------------------------------------------------
def error(bot, update, error):
    logger.error('Update "%s" caused error "%s"', update, error)


# ------------------------------------------------------------------------------------------------------
def main():
    logger.info("Bot Starts !")
    updater = Updater(config['DEFAULT']['token'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


# ------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()