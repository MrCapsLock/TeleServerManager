import configparser
import logging
import sqlite3

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, User, Bot

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


class User:
    # ------------------------------------------------------------------------------------------------------

    def fetch_from_db(self):
        connection = sqlite3.connect(config['DEFAULT']['database'])
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=={}".format(self.id))
        rows = cur.fetchall()
        if len(rows) == 0:
            logger.info("New User {} !".format(self.id))
            self.verify = False
            connection.close()
        else:
            self.verify = True
            connection.close()
        pass

    # ------------------------------------------------------------------------------------------------------
    def __call__(self, *args, **kwargs):
        pass

    # ------------------------------------------------------------------------------------------------------

    def __init__(self, usr: User):
        self.id = usr.id
        self.verify = False
        self.fetch_from_db()
