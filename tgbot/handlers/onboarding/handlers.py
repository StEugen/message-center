import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext


from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command
from tgbot.handlers.onboarding.manage_data import HELP

def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=make_keyboard_for_start_command())


def input_message_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == f'{HELP}':
        context.bot.send_message(
            chat_id=update.callback_query.message.chat_id, 
            text='Please enter your input',
            reply_to_message_id=update.callback_query.message.message_id)

def handle_input(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=user_input
    )