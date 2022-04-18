import emoji
from loguru import logger

from src.bot import bot
from src.constants import keyboards
from src.utils.filters import IsAdmin

# from src.utils.io import read_json_file, write_file, write_json_file


class Bot:
    """
    basic ready to go template for a Telegram Bot
    """

    def __init__(self, telebot) -> None:
        self.bot = telebot

        # add custom filters
        self.bot.add_custom_filter(IsAdmin())

        # register handlers
        self.handlers()

        # run bot
        logger.info('Bot is running...')
        self.bot.infinity_polling()

    def handlers(self):
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(
                message.chat.id, '<strong>You are admin of this group!</strong>')

        @self.bot.message_handler(func=lambda ـ: True)
        def echo(message):
            self.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
            )

    # personalized method for sending message to the client
    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        if emojize:
            text = emoji.emojize(text, use_aliases=True)

        self.bot.send_message(
            chat_id, text,
            reply_markup=reply_markup
        )


if __name__ == '__main__':
    bot = Bot(telebot=bot)
    bot.run()
