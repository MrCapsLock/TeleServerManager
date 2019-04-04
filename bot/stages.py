import configparser
import logging

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# ------------------------------------------------------------------------------------------------------
# Configuring bot
# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
try:
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))
except IOError:
    logger.error("Cant Open The Config File !")
    exit(1)


# ------------------------------------------------------------------------------------------------------

class Stages:
    # --------------------------------------------------

    @classmethod
    def main_menu(cls):
        kb = [
            [
                KeyboardButton(text="شورتکات ها"),
            ]
        ]
        return ReplyKeyboardMarkup(kb)

    # --------------------------------------------------

    def __init__(self):
        pass
